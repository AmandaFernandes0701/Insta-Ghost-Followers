# Insta Ghost Followers

## 📜 Table of Contents
1. [Introduction](#-introduction)
2. [Legal Notice and GDPR](#-legal-notice-and-gdpr)
3. [Instagram Terms of Use and Privacy](#-instagram-terms-of-use-and-privacy)
4. [Technologies Used](#-technologies-used)
5. [Project Structure](#-project-structure)
6. [How to Run the Project](#-how-to-run-the-project)
7. [Possible Improvements](#-possible-improvements)
8. [Lessons Learned](#-lessons-learned)
9. [References and Useful Links](#-references-and-useful-links)
10. [Contribution](#-contribution)

---

## 🌟 Introduction

**Insta Ghost Followers** is a simple and educational project developed to identify "ghost followers" on Instagram, i.e., people you follow but who don't follow you back. The project was created to explore the `instagrapi` library, which allows programmatic interaction with Instagram's API.

⚠️ **Warning**: This project is **for educational purposes only**. I do not recommend using it with personal accounts, as Instagram may block or suspend accounts that make excessive or improper use of its API. Always use a test or dummy account.

---

## ⚖️ Legal Notice and GDPR

### General Data Protection Regulation (GDPR)
This project was developed for studying and testing the `instagrapi` library. It does not collect, store, or share users' personal data. All information obtained is processed locally and is not persisted in any database or external service.

### Responsibility
The use of this project is entirely the user's responsibility. The developers are not responsible for any blocks, suspensions, or penalties applied by Instagram due to improper use of the API. I recommend that you read and understand [Instagram's Terms of Use](#-instagram-terms-of-use-and-privacy) before using this project.

---

## 📜 Instagram Terms of Use and Privacy

Instagram has strict policies regarding the use of its API. By using this project, you agree to the following terms:

1. **API Usage**: The project uses the `instagrapi` library to interact with Instagram. This library is not official and may violate Instagram's Terms of Service.
2. **Privacy**: Instagram prohibits the use of tools that collect user data without consent. This project does not collect data, but it is important to be aware of the platform's privacy policies.
3. **Limitations**: Instagram may block accounts that make too many requests in a short period. Use this project in moderation.

For more information, refer to [Instagram's Terms of Use](https://help.instagram.com/581066165581870) and [Privacy Policy](https://help.instagram.com/519522125107875).

---

## 🛠️ Technologies Used

- **Python**: Programming language used to develop the project.
- **Instagrapi**: Library that allows interaction with Instagram's API. [Official Repository](https://github.com/adw0rd/instagrapi).
- **Rich**: Library for displaying styled text in the terminal. [Official Repository](https://github.com/Textualize/rich).
- **Dotenv**: Library for managing environment variables. [Official Repository](https://github.com/theskumar/python-dotenv).

---

## 📂 Project Structure

The project is organized as follows:

```
Insta-Ghost-Followers/
├── .gitignore
├── main.py
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── auth.py
│   ├── analyzer.py
│   ├── utils.py
│   ├── config.py
│   └── exceptions.py
```

### File Descriptions

- **`.gitignore`**: Ignores unnecessary files and directories, such as `.env` and `__pycache__`.
- **`main.py`**: Entry point of the project. Contains the main logic for user interaction.
- **`requirements.txt`**: List of dependencies required to run the project.
- **`src/`**: Directory containing the project modules.
  - **`auth.py`**: Handles Instagram authentication.
  - **`analyzer.py`**: Contains the logic for analyzing "ghost followers."
  - **`utils.py`**: Utility functions, such as terminal text styling.
  - **`config.py`**: Global configurations, such as constants and logger.
  - **`exceptions.py`**: (Reserved for future exception handling implementations).

---

## 🚀 How to Run the Project

### Prerequisites

- Python 3.8 or higher.
- A test Instagram account (do not use your personal account).

### Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Insta-Ghost-Followers.git
   cd Insta-Ghost-Followers
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Instagram credentials:
   ```env
   INSTAGRAM_USERNAME=your_test_username
   INSTAGRAM_PASSWORD=your_test_password
   ```

4. Run the project:
   ```bash
   python main.py
   ```

5. Follow the instructions in the terminal to analyze "ghost followers."

---

## 🔧 Possible Improvements

- Add support for analyzing multiple accounts.
- Implement a caching system to avoid multiple API requests.
- Add more robust exception handling.
- Develop a simple graphical user interface (GUI) to make it easier to use.

---

## 📚 Lessons Learned

This project was a great opportunity to:
- Explore the `instagrapi` library and understand how to interact with unofficial APIs.
- Learn about development best practices, such as modularization and environment variable usage.
- Understand the limitations and risks of using tools that interact with platforms like Instagram.

---

## 🔗 References and Useful Links

- [Instagrapi Documentation](https://adw0rd.github.io/instagrapi/)
- [Instagrapi GitHub Repository](https://github.com/adw0rd/instagrapi)
- [Rich Documentation](https://rich.readthedocs.io/)
- [Instagram Terms of Use](https://help.instagram.com/581066165581870)
- [Instagram Privacy Policy](https://help.instagram.com/519522125107875)

---

## 🤝 Contribution

Contributions are welcome! If you'd like to improve this project, follow these steps:

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by [Amanda Fernandes]([https://github.com/your-username](https://github.com/AmandaFernandes0701)).  
📧 Contact: amandafernandesalves11@gmail.com  
🌐 LinkedIn: [Amanda Fernandes]([https://www.linkedin.com/in/your-profile/](https://www.linkedin.com/in/amanda-fernandes-software-engineer/))  

--- 

**Note**: This project is for educational purposes only. Use responsibly! 😊
