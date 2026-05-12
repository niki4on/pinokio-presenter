# Pinokio Presenter 🎬

A beautiful, easy-to-use presentation creation and viewing application for Pinokio AI.

## Features ✨

- **Create Presentations**: Build slides with titles, content, and different slide types
- **View Presentations**: Browse and navigate through your saved presentations
- **Edit Presentations**: Modify existing presentations
- **Export to PowerPoint**: Convert presentations to .pptx format
- **Web-Based UI**: Built with Streamlit for a smooth user experience
- **AI-Ready**: Fully integrated as a Pinokio app

## Installation

1. Open Pinokio
2. Click "Import App" or "Load from Folder"
3. Point to this repository folder
4. Click "Install" to install dependencies
5. Click "Run" to start the app

## Usage

### Creating a Presentation
1. Go to the "Create Presentation" tab
2. Enter your presentation title
3. Choose number of slides
4. Fill in each slide's title and content
5. Click "Save Presentation"

### Viewing Presentations
1. Go to the "View Presentations" tab
2. Select a presentation from the dropdown
3. Use the slider to navigate between slides
4. Export to PowerPoint if needed

### Editing Presentations
1. Go to the "Edit Presentation" tab
2. Select the presentation you want to edit
3. Modify slide content
4. Click "Save Changes"

## File Structure

```
pinokio-presenter/
├── pinokio.json          # Pinokio manifest
├── install.sh            # Installation script (Mac/Linux)
├── install.bat           # Installation script (Windows)
├── run.sh                # Run script (Mac/Linux)
├── run.bat               # Run script (Windows)
├── requirements.txt      # Python dependencies
├── app.py                # Main Streamlit application
├── README.md             # This file
└── presentations/        # Saved presentations (auto-created)
    ├── my_presentation.json
    └── my_presentation.pptx
```

## Requirements

- Python 3.8+
- Streamlit
- python-pptx
- Pillow
- Requests

## Customization

You can customize the appearance by modifying:
- Color scheme in the CSS section of `app.py`
- Font sizes in the Streamlit calls
- PowerPoint export settings in the `export_to_pptx()` function

## Tips

- Keep slide content concise for better presentations
- Use line breaks in content for better readability
- Export to PowerPoint for offline viewing or sharing
- Presentations are saved as JSON for easy backup

## License

MIT License - Feel free to modify and share!

## Support

For issues or feature requests, visit the repository or create an issue.