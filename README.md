# TweetWithMe 💬

Tweetify is a full-stack social media web application built using Django.

The application allows users to register, log in, create posts, like posts, comment in real-time, search content, and manage their own posts with proper authentication and authorization.

This project demonstrates backend architecture, database relationships, AJAX integration, and secure authentication handling using Django.

---

## 🚀 Core Features & Implementations

### 🔐 Authentication System
- User Registration
- Secure Login & Logout
- Password hashing using Django’s built-in authentication system
- Session management
- Access control (Only post owner can edit or delete their post)

---

### 📝 Post Management (CRUD Operations)
- Create new posts (with optional image upload)
- Edit posts (Owner only)
- Delete posts (Owner only)
- Display posts in responsive card layout
- Template inheritance for clean UI structure

---

### ❤️ Like System (AJAX – No Page Reload)
- Users can like and unlike posts
- ManyToMany relationship between User and Tweet model
- Real-time like count update using Fetch API
- CSRF protection implemented in AJAX requests

---

### 💬 Comment System (AJAX – No Page Reload)
- Users can add comments to posts
- Comments linked via ForeignKey to both User and Tweet
- Real-time comment rendering without page reload
- Scroll-friendly comment section UI

---

### 🔎 Search Functionality
- Search tweets by content
- Search users by username
- Implemented using Django ORM filtering

---

### 🎨 Frontend & UI
- Responsive design using Bootstrap 5
- Card-based layout for posts
- Animated hero section
- Interactive Like & Comment buttons
- Sticky footer layout
- Clean and modern dark theme UI

---

### 🗄 Database Design
- Custom Tweet model
- Comment model (ForeignKey relationships)
- ManyToMany relationship for Likes
- Proper relational database structure using Django ORM

---

### 🔐 Security Implementations
- CSRF protection enabled
- Login required decorators for restricted actions
- Owner-based permission control
- Secure form submission handling

---

## 🛠 Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap 5
- Database: SQLite (Development)
- JavaScript: Fetch API (AJAX)
- Version Control: Git & GitHub

## ⚙️ How To Run Locally

1. Clone the repository:

   git clone https://github.com/mohd-maruf-kureshi-2828/Tweety_full_stack_app/tree/main

2. Navigate into the project directory:

   cd tweety_full_stack_app

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   Windows:
   venv\Scripts\activate

   Mac/Linux:
   source venv/bin/activate

5. Install dependencies:

   pip install -r requirements.txt

6. Apply migrations:

   python manage.py migrate

7. Run the development server:

   python manage.py runserver

---

## 🌐 Deployment Status

This project is currently not deployed to a live hosting platform.

Reason:

Free hosting platforms often include limitations such as:
- Automatic sleep mode after inactivity
- Temporary or expiring databases
- Media file deletion on server restart

To ensure stable data integrity and avoid poor user experience caused by these limitations, the project is maintained locally and shared via GitHub for technical evaluation and code review.

The application is fully production-ready and can be deployed using PostgreSQL and cloud-based media storage when required.

---

## 📚 Key Learning Outcomes

- Understanding Django request-response lifecycle
- Implementing authentication and authorization
- Working with Model relationships (ForeignKey & ManyToMany)
- Integrating AJAX with Django backend
- Handling CSRF in asynchronous requests
- Structuring scalable Django applications
- Understanding development vs production environment differences

---

## 🔮 Future Improvements

- User Profile Page
- Follow / Unfollow System
- Notification System
- Pagination or Infinite Scroll
- Cloud media storage integration
- Full production deployment with PostgreSQL

---

## 👨‍💻 Author

Mohd Maruf Kureshi  
LinkedIn: https://www.linkedin.com/in/mohamed-maruf-kureshi-67357235b/?originalSubdomain=in
