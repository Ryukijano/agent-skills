#!/bin/bash
# Install all MCP servers into Cursor, Windsurf, Claude, Devin, and Gemini.
# Run: bash install_all.sh
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVERS_DIR="${SCRIPT_DIR}/servers"
PYTHON="$(which python3)"

echo "=== MCP Server Installer ==="
echo "Python: ${PYTHON}"
echo "Servers dir: ${SERVERS_DIR}"
echo ""

# Define servers
declare -A SERVERS
SERVERS["dgx-monitor"]="${SERVERS_DIR}/dgx_monitor/server.py"
SERVERS["cuda-profiling"]="${SERVERS_DIR}/cuda_profiling/server.py"
SERVERS["endosight-pipeline"]="${SERVERS_DIR}/endosight_pipeline/server.py"
SERVERS["research-workflow"]="${SERVERS_DIR}/research_workflow/server.py"
SERVERS["distributed-training"]="${SERVERS_DIR}/distributed_training/server.py"
SERVERS["cloud-gpu-ssh"]="${SERVERS_DIR}/cloud_gpu_ssh/server.py"
SERVERS["tpu-jax"]="${SERVERS_DIR}/tpu_jax/server.py"

# Define agent config files
declare -A CONFIGS
CONFIGS["Cursor"]="${HOME}/.cursor/mcp.json"
CONFIGS["Windsurf"]="${HOME}/.codeium/windsurf/mcp_config.json"
CONFIGS["Claude Code"]="${HOME}/.claude/mcp.json"
CONFIGS["Devin"]="${HOME}/.config/devin/mcp_config.json"
CONFIGS["Gemini"]="${HOME}/.gemini/config/mcp_config.json"

# Function to merge a server into a JSON config file
merge_server_into_config() {
    local config_file="$1"
    local server_name="$2"
    local server_path="$3"

    # Create config if it doesn't exist
    if [ ! -f "$config_file" ]; then
        mkdir -p "$(dirname "$config_file")"
        echo '{"mcpServers": {}}' > "$config_file"
    fi

    # Use python to safely merge JSON
    python3 -c "
import json, sys, os, glob, subprocess
config_path = sys.argv[1]
server_name = sys.argv[2]
server_path = sys.argv[3]

def find_torch_python():
    candidates = []
    mcp_bin = os.environ.get('MCP_PYTHON_BIN')
    if mcp_bin:
        candidates.append(mcp_bin)
    for p in glob.glob(os.path.expanduser('~/.conda/envs/*/bin/python*')):
        if os.path.isfile(p) and os.access(p, os.X_OK):
            candidates.append(p)
    for p in glob.glob(os.path.expanduser('~/miniconda3/envs/*/bin/python*')):
        if os.path.isfile(p) and os.access(p, os.X_OK):
            candidates.append(p)
    for p in glob.glob(os.path.expanduser('~/anaconda3/envs/*/bin/python*')):
        if os.path.isfile(p) and os.access(p, os.X_OK):
            candidates.append(p)
    for p in glob.glob('/opt/conda/envs/*/bin/python*'):
        if os.path.isfile(p) and os.access(p, os.X_OK):
            candidates.append(p)
    for p in glob.glob(os.path.expanduser('~/.pyenv/versions/*/bin/python*')):
        if os.path.isfile(p) and os.access(p, os.X_OK):
            candidates.append(p)
    for p in candidates:
        try:
            r = subprocess.run([p, '-c', 'import torch; print(\"ok\")'], capture_output=True, text=True, timeout=5)
            if r.returncode == 0 and 'ok' in r.stdout:
                return p
        except Exception:
            continue
    return None

with open(config_path) as f:
    config = json.load(f)

if 'mcpServers' not in config:
    config['mcpServers'] = {}

server_entry = {
    'command': 'python3',
    'args': [server_path]
}

if server_name == 'distributed-training':
    torch_python = find_torch_python()
    if torch_python:
        server_entry['env'] = {'MCP_PYTHON_BIN': torch_python}

config['mcpServers'][server_name] = server_entry

with open(config_path, 'w') as f:
    json.dump(config, f, indent=2)

print(f'  Added {server_name} -> {config_path}')
" "$config_file" "$server_name" "$server_path"
}

# Install each server into each agent
for server_name in "${!SERVERS[@]}"; do
    server_path="${SERVERS[$server_name]}"
    if [ ! -f "$server_path" ]; then
        echo "WARNING: Server file not found: $server_path"
        continue
    fi
    echo "Installing: ${server_name}"
    for agent_name in "${!CONFIGS[@]}"; do
        config_file="${CONFIGS[$agent_name]}"
        merge_server_into_config "$config_file" "$server_name" "$server_path"
    done
    echo ""
done

echo "=== Installation complete ==="
echo ""
echo "To test a server in CLI mode:"
echo "  python3 ${SERVERS_DIR}/dgx_monitor/server.py --cli gpu_status"
echo "  python3 ${SERVERS_DIR}/cuda_profiling/server.py --cli memcheck --command ./my_kernel"
echo ""
echo "To test with MCP Inspector:"
echo "  npx @modelcontextprotocol/inspector python3 ${SERVERS_DIR}/dgx_monitor/server.py"
echo ""
echo "Restart your AI coding agents (Cursor, Windsurf, etc.) to pick up the new MCP servers."
