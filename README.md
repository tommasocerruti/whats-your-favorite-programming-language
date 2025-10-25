# What's Your Favorite Programming Language? 📊

An interactive web application that collects and visualizes programming language preferences through real-time pie charts. Users can vote for their favorite language and instantly see how their choice compares to others.

![Demo](https://img.shields.io/badge/demo-live-brightgreen) ![Python](https://img.shields.io/badge/python-3.x-blue) ![Flask](https://img.shields.io/badge/flask-3.0.3-lightgrey)

## ✨ Features

- **Interactive Voting**: Choose from 23+ popular programming languages
- **Real-time Visualization**: Pie chart updates instantly after each vote
- **Secure Backend**: Input validation and NoSQL injection protection
- **Responsive Design**: Works on desktop and mobile devices
- **Persistent Storage**: Data saved in MongoDB or in-memory for testing

## 🛠 Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Chart.js for visualizations)
- **Backend**: Flask (Python web framework)
- **Database**: MongoDB (with in-memory fallback option)
- **Security**: Input sanitization, CORS protection, error handling

## 🚀 Quick Start

### Option 1: With MongoDB (Recommended)

1. **Clone and setup**:
   ```bash
   git clone https://github.com/tommasocerruti/whats-your-favorite-programming-language.git
   cd whats-your-favorite-programming-language
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Install MongoDB**:
   ```bash
   # macOS with Homebrew
   brew tap mongodb/brew
   brew install mongodb-community
   brew services start mongodb/brew/mongodb-community
   
   # Or use Docker
   docker run -d -p 27017:27017 --name mongodb mongo:latest
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

### Option 2: Quick Test (No MongoDB Required)

1. **Setup and run**:
   ```bash
   git clone https://github.com/tommasocerruti/whats-your-favorite-programming-language.git
   cd whats-your-favorite-programming-language
   pip install flask flask-cors
   python app_simple.py
   ```

2. **Access the app**: Open `http://127.0.0.1:5000/`

## 📱 How to Use

1. **Vote**: Select your favorite programming language from the dropdown
2. **Submit**: Click the "Submit" button to cast your vote
3. **Visualize**: Watch the pie chart update in real-time
4. **Explore**: Vote multiple times to see the distribution change

### Available Languages
C, C++, Java, Python, JavaScript, Ruby, Swift, Go, Kotlin, TypeScript, PHP, R, Scala, Perl, Objective-C, Shell, MATLAB, Dart, Elixir, Rust, Haskell, Lua, F#

## 🔧 API Endpoints

- `GET /` - Main application page
- `POST /submit` - Submit language vote
  ```json
  {"language": "Python"}
  ```
- `GET /languages` - Get current vote counts
  ```json
  {"Python": 15, "JavaScript": 12, "Java": 8}
  ```

## 🔒 Security Features

- Input validation and sanitization
- NoSQL injection prevention
- CORS protection
- Error handling and logging
- Rate limiting ready

## 🐛 Troubleshooting

**MongoDB Connection Issues**:
- Ensure MongoDB is running: `brew services list | grep mongodb`
- Check connection string in environment variables
- Use `app_simple.py` for testing without MongoDB

**Port Already in Use**:
- Kill existing process: `lsof -ti:5000 | xargs kill -9`
- Or change port in app configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Tommaso Cerruti**
- Email: [tommasocerruti@gmail.com](mailto:tommasocerruti@gmail.com)
- GitHub: [@tommasocerruti](https://github.com/tommasocerruti)

---

⭐ **Star this repo if you found it helpful!**