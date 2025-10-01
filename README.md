# Sports Committee Chatbot 🏆

An AI-powered chatbot designed to assist students with Sports Committee information, built with React frontend and FastAPI backend using Google's Gemini AI.

## 🚀 Features

- **Intelligent Sports Assistant**: AI-powered responses about sports committee activities, events, and policies
- **Natural Language Processing**: Supports both English and Hinglish queries
- **Real-time Chat Interface**: Modern, responsive web interface built with React
- **Smart Context Awareness**: Uses context from sports committee documentation
- **Profanity Filter**: Maintains appropriate conversation standards
- **Committee Comparison**: Promotes sports committee while respectfully discussing other committees

## 🛠️ Tech Stack

### Frontend
- **React 19** - Modern UI framework
- **Vite** - Fast build tool
- **TailwindCSS** - Utility-first CSS framework
- **Axios** - HTTP client for API communication
- **React Markdown** - Markdown rendering support
- **Lucide React** - Icon library

### Backend
- **FastAPI** - Modern Python web framework
- **Google Gemini AI** - Advanced language model
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **Google Gemini API Key**

## 🏃‍♂️ Getting Started

### 1. Clone the Repository
```bash
git clone <repository-url>
cd sports-spit-chatbot
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
```

Edit the `.env` file and add your configuration:
```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
API_TEMPERATURE=0.3
API_MAX_TOKENS=500
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
HOST=0.0.0.0
PORT=8000
RELOAD=true
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create environment file
cp .env.example .env.local
```

Edit the `.env.local` file:
```env
VITE_API_URL=http://localhost:8000
```

### 4. Running the Application

**Start the backend:**
```bash
cd backend
python main.py
```
The API will be available at `http://localhost:8000`

**Start the frontend (in another terminal):**
```bash
cd frontend
npm run dev
```
The app will be available at `http://localhost:5173`

## 📚 API Documentation

### Endpoints

#### `GET /`
- **Description**: Root endpoint
- **Response**: Welcome message

#### `GET /health`
- **Description**: Health check
- **Response**: Service status and bot readiness

#### `POST /chat`
- **Description**: Main chat endpoint
- **Request Body**:
  ```json
  {
    "message": "Your question here"
  }
  ```
- **Response**:
  ```json
  {
    "response": "AI-generated response"
  }
  ```

#### `POST /keep-alive`
- **Description**: Keep-alive endpoint for deployment platforms
- **Response**: Server status and timestamp

### Interactive API Documentation
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🎯 Usage Examples

**General Sports Questions:**
```
User: "What is agility in sports?"
Bot: "Agility in sports refers to the ability to change direction quickly..."
```

**Event Information:**
```
User: "When is the next football tournament?"
Bot: "Seniors will post the final dates on official class groups."
```

**Committee Information:**
```
User: "How can I join the sports committee?"
Bot: "To join the sports committee, you need to..."
```

**Greetings & Small Talk:**
```
User: "Hi"
Bot: "Hey! 👋"

User: "Thanks"
Bot: "Anytime!"
```

## 🗂️ Project Structure

```
sports-spit-chatbot/
├── backend/
│   ├── main.py           # FastAPI application entry point
│   ├── bot.py            # Chatbot logic and Gemini AI integration
│   ├── requirements.txt  # Python dependencies
│   ├── .env             # Environment variables (create from .env.example)
│   └── context.txt      # Sports committee knowledge base
├── frontend/
│   ├── src/
│   │   ├── App.jsx      # Main React component
│   │   ├── main.jsx     # React entry point
│   │   └── index.css    # Global styles
│   ├── package.json     # Node.js dependencies
│   ├── vite.config.js   # Vite configuration
│   └── tailwind.config.js # TailwindCSS configuration
├── .gitignore           # Git ignore rules
└── README.md           # This file
```

## 🌐 Deployment

### Backend Deployment (Render/Heroku)

1. **Environment Variables**: Set all required environment variables
2. **Start Command**: `python main.py`
3. **Health Check**: The `/health` endpoint provides service status
4. **Keep-Alive**: Use `/keep-alive` endpoint to prevent service sleeping

### Frontend Deployment (Vercel/Netlify)

1. **Build Command**: `npm run build`
2. **Output Directory**: `dist`
3. **Environment Variables**: Set `VITE_API_URL` to your backend URL

## ⚙️ Configuration

### Environment Variables

**Backend (.env):**
- `GEMINI_API_KEY`: Your Google Gemini API key
- `GEMINI_MODEL`: Gemini model to use (default: gemini-2.5-flash)
- `API_TEMPERATURE`: Response creativity (0-1, default: 0.3)
- `API_MAX_TOKENS`: Max response length (default: 500)
- `ALLOWED_ORIGINS`: CORS allowed origins
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)

**Frontend (.env.local):**
- `VITE_API_URL`: Backend API URL

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

**Backend won't start:**
- Verify Python version (3.8+)
- Check if all dependencies are installed
- Ensure GEMINI_API_KEY is set in .env

**Frontend can't connect to backend:**
- Verify VITE_API_URL in .env.local
- Check if backend is running on the correct port
- Verify CORS settings in backend

**AI responses are slow/not working:**
- Check Gemini API key validity
- Verify internet connection
- Check API quotas and limits

### Getting Help

- Check the [Issues](../../issues) page for common problems
- Create a new issue if you encounter a bug
- Contact the development team for additional support

---

Built with ❤️ for the Sports Committee by the development team.
