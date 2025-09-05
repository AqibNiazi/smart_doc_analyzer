# Smart Document Analyzer

A beautiful web interface for document analysis that extracts text, generates summaries, and creates audio from your documents.

## Features

- **Modern React Frontend**: Beautiful, responsive UI with animations and real-time feedback
- **Flask Backend**: RESTful API with document processing capabilities
- **Multi-format Support**: PDF, DOCX, and TXT file processing
- **AI-Powered Summarization**: Integration with Grok and Hugging Face APIs
- **Text-to-Speech**: Convert summaries to audio using Google TTS
- **Professional Design**: Clean, modern interface with gradient backgrounds and smooth transitions

## Project Structure

```
smart-document-analyzer/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/      # UI components
│   │   ├── App.jsx         # Main application component
│   │   ├── App.css         # Application styles
│   │   └── main.jsx        # Entry point
│   ├── index.html          # HTML template
│   ├── package.json        # Frontend dependencies
│   └── vite.config.js      # Vite configuration
├── backend/                 # Flask backend application
│   ├── src/
│   │   ├── routes/         # API routes
│   │   ├── models/         # Database models
│   │   ├── static/         # Static files (built frontend)
│   │   └── main.py         # Flask application
│   ├── requirements.txt    # Python dependencies
│   └── venv/              # Virtual environment
└── README.md              # This file
```

## Setup Instructions

### Prerequisites

- Node.js (v18 or higher)
- Python (v3.8 or higher)
- npm or pnpm

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (create a `.env` file):
   ```
   XAI_API_KEY=your_grok_api_key_here
   HUGGINGFACE_API_KEY=your_huggingface_api_key_here
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   pnpm install
   ```

### Development Mode

#### Option 1: Separate Frontend and Backend (Development)

1. Start the backend server:
   ```bash
   cd backend
   source venv/bin/activate
   python src/main.py
   ```
   Backend will run on http://localhost:5000

2. Start the frontend development server:
   ```bash
   cd frontend
   npm run dev
   # or
   pnpm run dev
   ```
   Frontend will run on http://localhost:5173

#### Option 2: Integrated Deployment (Production)

1. Build the frontend:
   ```bash
   cd frontend
   npm run build
   # or
   pnpm run build
   ```

2. Copy built files to backend static directory:
   ```bash
   cp -r frontend/dist/* backend/src/static/
   ```

3. Start the integrated Flask server:
   ```bash
   cd backend
   source venv/bin/activate
   python src/main_integrated.py
   ```
   Application will run on http://localhost:5001

## API Configuration

The application supports two LLM backends:

### Grok API
- Get your API key from: https://console.groq.com/
- Set the `XAI_API_KEY` environment variable

### Hugging Face API
- Get your API key from: https://huggingface.co/settings/tokens
- Set the `HUGGINGFACE_API_KEY` environment variable

## Usage

1. Open the application in your browser
2. Configure your API settings in the left panel:
   - Select LLM Backend (Grok or Hugging Face)
   - Enter your API key
   - Choose audio language
3. Upload a document (PDF, DOCX, or TXT)
4. Click "Extract Text" to process the document
5. Click "Generate Summary" to create an AI summary
6. Click "Generate Audio" to convert the summary to speech
7. Use the audio player to listen or download the audio file

## File Support

- **PDF**: Extracts text using pdfplumber
- **DOCX**: Extracts text using python-docx
- **TXT**: Direct text file reading

## Technologies Used

### Frontend
- React 18
- Vite
- Tailwind CSS
- shadcn/ui components
- Framer Motion (animations)
- Lucide React (icons)

### Backend
- Flask
- Flask-CORS
- pdfplumber (PDF processing)
- python-docx (DOCX processing)
- OpenAI SDK (Grok API)
- requests (Hugging Face API)
- gTTS (Google Text-to-Speech)

## Deployment

For production deployment:

1. Build the frontend and integrate with backend (see Option 2 above)
2. Set up environment variables on your server
3. Use a production WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 src.main_integrated:app
   ```

## Troubleshooting

### Common Issues

1. **CORS Errors**: Make sure Flask-CORS is installed and configured
2. **API Key Errors**: Verify your API keys are correct and have sufficient credits
3. **File Upload Issues**: Check file size limits and supported formats
4. **Audio Generation Fails**: Ensure gTTS can access Google's servers

### Error Messages

- "No text found in document": The document may be image-based or corrupted
- "API key required": Enter a valid API key in the settings panel
- "Failed to generate summary": Check your API key and internet connection

## License

This project is open source and available under the MIT License.

