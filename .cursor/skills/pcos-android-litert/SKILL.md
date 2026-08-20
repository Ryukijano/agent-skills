# Android LiteRT-LM for PCOS

PCOS on Android uses **LiteRT-LM v0.13+** for on-device inference with Gemma 4 and FunctionGemma models.

## Models

| Model | Size | Use Case | Download Source |
|-------|------|----------|-----------------|
| FunctionGemma 270M | ~270MB | Fast function calling | HuggingFace LiteRT Community |
| Gemma 4 E2B | ~2GB | Full inference for complex tasks | HuggingFace LiteRT Community |

## Architecture

- **LiteRTManager** — Manages Engine, Conversation, and ToolSet lifecycle
- **PCOSService** — Foreground service, pre-downloads models on startup
- **BridgeClient** — WebSocket client with exponential backoff reconnection
- **PCOSViewModel** — MVVM bridge between service and Compose UI

## Tool Use API (FunctionGemma)

```kotlin
@Tool("Save a note to memory")
fun saveNote(
    @ToolParam("The note content") content: String,
    @ToolParam("Optional category") category: String = "general"
): String {
    // Save to PiecesOS or local storage
    return "Note saved: $content"
}

@Tool("Create a task reminder")
fun createTask(
    @ToolParam("Task description") description: String,
    @ToolParam("Due time (ISO)") dueTime: String? = null
): String {
    return "Task created: $description"
}
```

## Streaming Inference

```kotlin
session.generateStreaming(prompt).collect { token ->
    // Update UI with each token
    _uiState.update { it.copy(output = it.output + token) }
}
```

## Model Download Flow

1. Check if `.litertlm` file exists in app data dir
2. If not, download from HuggingFace with progress callback
3. Write to safe tmp file first, then rename (atomic)
4. Load Engine from file path
5. Create Session/Conversation/ToolSet

## GPU Backend

Native libraries in AndroidManifest:
```xml
<uses-native-library android:name="libvndksupport.so" android:required="false" />
<uses-native-library android:name="libOpenCL.so" android:required="false" />
```

## Key Files

- `apps/android/app/build.gradle.kts` — Dependencies (LiteRT-LM 0.13.1)
- `apps/android/app/src/main/java/com/pcos/edge/LiteRTManager.kt` — Engine/session management
- `apps/android/app/src/main/java/com/pcos/edge/PCOSService.kt` — Foreground service
- `apps/android/app/src/main/java/com/pcos/edge/BridgeClient.kt` — WebSocket client
- `apps/android/app/src/main/java/com/pcos/edge/PCOSViewModel.kt` — MVVM ViewModel
- `apps/android/app/src/main/java/com/pcos/edge/MainActivity.kt` — Compose UI
- `apps/android/app/src/main/AndroidManifest.xml` — Permissions and components

## Build

```bash
cd apps/android
./gradlew assembleDebug
```

Requires Android SDK 34+, Kotlin 2.0, minSdk 24.
