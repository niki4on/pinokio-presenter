#!/usr/bin/env python3
"""
Simple AI Presentation Generator
One prompt -> Full presentation with one click
"""

import os
import json
from pathlib import Path
from datetime import datetime
import subprocess
import sys

try:
    from anthropic import Anthropic
except ImportError:
    print("Installing required package...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "anthropic"])
    from anthropic import Anthropic


def get_api_key():
    """Get Claude API key from environment or user"""
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        print("\n🔑 You need a free Claude API key from Anthropic")
        print("Get it here: https://console.anthropic.com/keys")
        key = input("\nPaste your API key: ").strip()
        if not key:
            print("❌ API key required!")
            sys.exit(1)
    return key


def generate_presentation(prompt: str, api_key: str) -> dict:
    """Generate presentation using Claude"""
    client = Anthropic()
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": f"""Create a professional presentation outline as JSON with this exact structure:
{{
  "title": "Presentation Title",
  "slides": [
    {{"title": "Slide Title", "content": "Bullet points or text here"}},
    ...
  ]
}}

User request: {prompt}

Create 5-7 slides. Return ONLY valid JSON, no other text."""
            }
        ]
    )
    
    # Parse response
    response_text = message.content[0].text
    
    # Extract JSON
    try:
        start = response_text.find('{')
        end = response_text.rfind('}') + 1
        json_str = response_text[start:end]
        return json.loads(json_str)
    except (json.JSONDecodeError, ValueError):
        print(f"❌ Failed to parse response: {response_text}")
        return None


def save_presentation(presentation: dict, save_path: Path) -> Path:
    """Save presentation as JSON"""
    save_path.mkdir(parents=True, exist_ok=True)
    
    filename = presentation['title'].replace(" ", "_").replace("/", "-")
    filepath = save_path / f"{filename}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(filepath, 'w') as f:
        json.dump(presentation, f, indent=2)
    
    return filepath


def export_to_html(presentation: dict, filepath: Path) -> Path:
    """Export presentation to HTML"""
    html_path = filepath.with_suffix('.html')
    
    slides_html = ""
    for i, slide in enumerate(presentation['slides'], 1):
        slides_html += f"""
        <div class="slide">
            <div class="slide-number">{i}/{len(presentation['slides'])}</div>
            <h2>{slide['title']}</h2>
            <p>{slide['content']}</p>
        </div>
        """
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{presentation['title']}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{
            width: 100%;
            max-width: 900px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .slides {{
            display: flex;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
        }}
        .slide {{
            min-width: 100%;
            padding: 80px 40px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            scroll-snap-align: start;
            position: relative;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }}
        .slide:nth-child(even) {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}
        .slide h2 {{
            font-size: 2.5em;
            margin-bottom: 30px;
            color: #333;
        }}
        .slide:nth-child(even) h2 {{
            color: white;
        }}
        .slide p {{
            font-size: 1.2em;
            line-height: 1.6;
            color: #666;
        }}
        .slide:nth-child(even) p {{
            color: #f0f0f0;
        }}
        .slide-number {{
            position: absolute;
            top: 20px;
            right: 30px;
            font-size: 0.9em;
            opacity: 0.6;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .controls {{
            background: #f5f7fa;
            padding: 20px;
            text-align: center;
            font-size: 0.9em;
        }}
        .controls p {{
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{presentation['title']}</h1>
        </div>
        <div class="slides">
            {slides_html}
        </div>
        <div class="controls">
            <p>💡 Scroll left/right to navigate slides | 🖨️ Use browser print to save as PDF</p>
        </div>
    </div>
</body>
</html>"""
    
    with open(html_path, 'w') as f:
        f.write(html)
    
    return html_path


def display_presentation(presentation: dict):
    """Display presentation in terminal"""
    print("\n" + "="*60)
    print(f"📊 {presentation['title']}")
    print("="*60)
    for i, slide in enumerate(presentation['slides'], 1):
        print(f"\n🔹 Slide {i}: {slide['title']}")
        print(f"   {slide['content']}")
    print("\n" + "="*60)


def main():
    print("\n" + "🎬 "*10)
    print("   AI PRESENTATION GENERATOR")
    print("🎬 "*10 + "\n")
    
    # Get API key
    api_key = get_api_key()
    
    # Get user prompt
    print("\n📝 What presentation do you want to create?")
    print("Example: 'Create a presentation about AI in healthcare with pros and cons'\n")
    prompt = input("Your idea: ").strip()
    
    if not prompt:
        print("❌ Please provide a presentation idea!")
        sys.exit(1)
    
    # Get save path
    print("\n📁 Where do you want to save it?")
    print(f"Default: {Path.home() / 'Presentations'}")
    save_path_input = input("Path (or press Enter for default): ").strip()
    
    if save_path_input:
        save_path = Path(save_path_input).expanduser()
    else:
        save_path = Path.home() / "Presentations"
    
    # Generate
    print("\n⏳ Generating presentation with AI...")
    presentation = generate_presentation(prompt, api_key)
    
    if not presentation:
        print("❌ Failed to generate presentation!")
        sys.exit(1)
    
    # Save
    print("💾 Saving...")
    json_path = save_presentation(presentation, save_path)
    html_path = export_to_html(presentation, json_path)
    
    # Display
    display_presentation(presentation)
    
    # Results
    print(f"\n✅ Presentation created!\n")
    print(f"📄 JSON: {json_path}")
    print(f"🌐 HTML: {html_path}")
    print(f"\n💡 Open the HTML file in your browser to view!")
    print(f"🖨️  You can print to PDF from the browser too.\n")
    
    # Ask to open
    try:
        import webbrowser
        webbrowser.open(f'file://{html_path}')
    except:
        pass


if __name__ == "__main__":
    main()
