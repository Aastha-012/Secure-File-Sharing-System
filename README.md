# Secure-File-Sharing-System
A Flask-based secure file-sharing system with role-based access. Operations Users can upload .pptx, .docx, and .xlsx files, while Client Users can sign up, verify emails, and securely download files via encrypted links. Includes REST APIs, test cases, and a Postman collection.

Features
	•	Role-based access for Operations and Client Users.
	•	Operations Users can upload files in .pptx, .docx, and .xlsx formats.
	•	Client Users can sign up, verify email, and download files through secure, encrypted links.
	•	Includes test cases for API functionality and a Postman collection for API testing.

Technologies Used
	•	Flask: Python web framework for building APIs.
	•	Flask-SQLAlchemy: ORM for database interaction.
	•	Flask-Mail: For email verification.
	•	SQL Database: For user and file data storage.

Installation

Prerequisites
	•	Python 3.8 or higher

 API Endpoints
	•	POST /signup: Register a new Client User.
	•	POST /login: Login for both Operations and Client Users.
	•	POST /upload: Upload a file (accessible only by Operations Users).
	•	GET /download-file/{id}: Download a file with an encrypted link (accessible by Client Users).
	•	GET /list-files: List all uploaded files (accessible by Client Users).

Testing
	•	Test the APIs using the provided Postman collection.
	•	Test cases for API functionality are included in the repository.
