# Meme Engine Progress Tracker

## Project Context

| Topic | Status | Notes |
|---|---|---|
| Module responsibility | Active | The Meme Engine Module is responsible for manipulating an image and drawing quote text onto it. |
| Design goal | Active | This module reinforces object-oriented thinking while using a third-party image library for image manipulation. |
| Main library | Active | The project expects use of Pillow (`PIL`) for loading, resizing, drawing text, and saving images. |
| Core method | Active | The class must implement `make_meme(self, img_path, text, author, width=500) -> str`. |
| Output goal | Active | The method should return the path to the manipulated image after the meme is created and saved. |

## Functionality

| Task | Status | Notes |
|---|---|---|
| Create Meme Engine class | Pending | Implement the class responsible for generating memes. |
| Load image with Pillow | Pending | Load an image using Pillow (`PIL`). |
| Resize image | Pending | Resize the image so the width is at most `500px` and the height scales proportionally. |
| Add quote body text | Pending | Draw the quote body onto the image. |
| Add quote author text | Pending | Draw the quote author onto the image. |
| Save manipulated image | Pending | Save the manipulated image to disk. |
| Implement `make_meme` method | Pending | Implement `make_meme(self, img_path, text, author, width=500) -> str`. |
| Return output path | Pending | Return the path to the saved meme image. |
| Check against rubric | Pending | Compare implementation against the Meme Generator Module rubric if needed. |

## Style

| Task | Status | Notes |
|---|---|---|
| Add clear docstrings | Pending | All Meme Generator classes should have clear, concise, and PEP-compliant docstrings. |
| Check PEP 8 compliance | Pending | All code should be PEP 8 compliant. |
| Handle common exceptions | Pending | Common exceptions should be handled using try-catch blocks. |
| Remove starter comments | Pending | No `TODO` markers should remain in submitted code. |

## Validation

| Check | Status | Notes |
|---|---|---|
| Image loads successfully | Pending | Confirm the engine can open a valid image path. |
| Image resizes correctly | Pending | Confirm width is capped at `500` and aspect ratio is preserved. |
| Text is drawn on image | Pending | Confirm quote body and author appear on the image. |
| Image saves successfully | Pending | Confirm the manipulated image is written to disk. |
| `make_meme()` returns output path | Pending | Confirm the method returns the saved image path as a string. |
