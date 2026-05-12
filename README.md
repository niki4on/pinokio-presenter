# Pinokio Presenter 🎬

A beautiful, easy-to-use presentation creation and viewing application for Pinokio AI with AI-powered content generation.

## Features ✨

- **Create Presentations**: Build slides with titles, content, and different slide types
- **View Presentations**: Browse and navigate through your saved presentations
- **Edit Presentations**: Modify existing presentations
- **AI Assistant**: Generate presentation content using local AI models (Ollama, LM Studio, etc.)
- **Templates**: Pre-designed presentation templates for common use cases
- **Multiple Export Formats**: PowerPoint (.pptx), HTML, and JSON
- **Web-Based UI**: Built with Streamlit for a smooth user experience
- **Fully Local**: Everything runs on your computer with no cloud dependencies

## Features in Detail

### 📋 Templates
Choose from professionally designed templates:
- **Business Pitch** - Perfect for startup pitches and business presentations
- **Educational** - Great for teaching and academic content
- **Project Report** - Ideal for status updates and project presentations
- **Conference Talk** - Professional setup for keynotes and talks

### 🤖 AI Assistant
- Generate presentation outlines based on topics
- Get slide ideas and content suggestions
- Polish and enhance your content (requires local AI model)
- Integration with Pinokio's available models

### 💾 Export Options
- **PowerPoint** - Professional .pptx format for sharing
- **HTML** - Web-viewable presentations with print support
- **JSON** - Data format for backup and integration

## Installation

### Quick Start with Pinokio

1. Open Pinokio
2. Click "Import App" or "Load from Folder"
3. Point to this repository folder: `https://github.com/niki4on/pinokio-presenter`
4. Click "Install" to install dependencies
5. Click "Run" to start the app

### Manual Installation

1. Clone this repository:
```bash
git clone https://github.com/niki4on/pinokio-presenter.git
cd pinokio-presenter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Usage

### Creating a Presentation

1. Go to the **"Create Presentation"** tab
2. Enter your presentation title
3. Choose number of slides
4. Fill in each slide's title, type, and content
5. Click **"Save Presentation"**
6. Export in your preferred format

### Using Templates

1. Go to the **"Templates"** tab
2. Select a template that fits your needs
3. Give your presentation a name
4. Click **"Create from Template"**
5. Edit the slides in the **"Edit Presentation"** tab

### AI Assistant

1. Go to the **"AI Assistant"** tab
2. Choose an option:
   - **Generate Presentation Content**: Create full presentations from a topic
   - **Generate Slide Ideas**: Get suggestions for your presentation structure
   - **Polish Content**: Enhance existing slide content
3. Note: AI features require a local language model running in Pinokio

### Viewing & Editing

1. **View**: Go to "View Presentations" tab
   - Select a presentation
   - Use the slider to navigate slides
   - Export to PowerPoint, HTML, or JSON
   - Delete presentations

2. **Edit**: Go to "Edit Presentation" tab
   - Select a presentation to edit
   - Modify any slide's title, type, or content
   - Click "Save Changes"

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
    ├── my_presentation.pptx
    ├── my_presentation.html
    └── images/           # Generated images for slides
```

## Requirements

- Python 3.8+
- Streamlit >= 1.28.0
- python-pptx >= 0.6.21
- Pillow >= 10.0.0
- Requests >= 2.31.0

Optional (for AI features):
- Ollama, LM Studio, or other local LLM running on standard ports
- Stable Diffusion or other image generation model in Pinokio

## Configuration

### Customizing Appearance

Edit the CSS section in `app.py`:
```python
st.markdown("""
<style>
    .main-header {
        color: #FF6B6B;  # Change to your preferred color
    }
    ...
</style>
""", unsafe_allow_html=True)
```

### Adding Custom Templates

Edit the `TEMPLATES` dictionary in `app.py`:
```python
TEMPLATES = {
    "My Custom Template": {
        "slides": [
            {"title": "Slide 1", "content": "Content here", "type": "Title Slide"},
            # Add more slides...
        ]
    }
}
```

### AI Model Configuration

To use AI features, ensure a local model is running:

**For text generation (Ollama):**
```bash
ollama pull mistral
ollama serve
```

**For image generation (Stable Diffusion):**
Install and run through Pinokio's model hub.

## Tips for Great Presentations

- **Keep it concise**: Use bullet points instead of paragraphs
- **Use visuals**: The app supports images in content areas
- **Consistent design**: Stick to one font and color scheme
- **Tell a story**: Organize slides in a logical flow
- **Practice**: Review your slides before presenting
- **Export early**: Keep multiple formats for different audiences

## Keyboard Shortcuts

When viewing presentations:
- **Arrow Keys**: Navigate between slides
- **Spacebar**: Next slide (in HTML export)
- **1-9**: Jump to slide number (in HTML export)

## Troubleshooting

### App won't start
- Ensure Python 3.8+ is installed
- Run: `pip install -r requirements.txt`
- Check that port 8501 is not in use

### Presentations not saving
- Check that the `presentations/` directory exists and is writable
- Ensure you have disk space available
- Try saving with a different name

### AI features not working
- Verify a local AI model is running in Pinokio
- Check the correct endpoint is configured
- See logs for connection errors

### Export to PowerPoint fails
- Update python-pptx: `pip install --upgrade python-pptx`
- Try exporting to HTML instead
- Check available disk space

## Privacy & Security

- ✅ All presentations are saved locally on your computer
- ✅ No data is sent to external servers
- ✅ No account or login required
- ✅ Full control over your data

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

- [ ] Real-time collaboration features
- [ ] More AI model integrations
- [ ] Animated transitions support
- [ ] Speaker notes
- [ ] Presentation timer
- [ ] Voice narrator integration
- [ ] PDF export with speaker notes
- [ ] Cloud sync optional backup
- [ ] Presentation analytics
- [ ] Theme customization UI

## License

MIT License - Feel free to modify and share! See LICENSE file for details.

## Support

- 📖 [Documentation](https://github.com/niki4on/pinokio-presenter)
- 🐛 [Report Issues](https://github.com/niki4on/pinokio-presenter/issues)
- 💡 [Suggest Features](https://github.com/niki4on/pinokio-presenter/discussions)

## Credits

Made for [Pinokio](https://pinokio.computer/) - The AI Browser

Built with:
- [Streamlit](https://streamlit.io/) - Web app framework
- [python-pptx](https://python-pptx.readthedocs.io/) - PowerPoint generation
- [Pillow](https://python-pillow.org/) - Image processing

---

**Enjoy creating beautiful presentations! 🎉**
