# 🍽️ ResMan - Restaurant Management & Waiter Dashboard

ResMan is a clean, fast, and modern restaurant management system designed for waiters to track real-time table occupancy, place orders effortlessly, and manage guest reservations.

This project combines a robust backend API infrastructure with an interactive and responsive frontend dashboard.

---

## 📸 Screenshots

Here is a quick look at the ResMan interface:

### 1. Secure Authentication (Sign In)
*Sign in using your waiter or manager credentials to access the dashboard.*
<img width="1116" height="867" alt="Screenshot 2026-07-15 113214" src="https://github.com/user-attachments/assets/b146c63a-601e-47f3-bbf7-c370c5d4c7c9" />

### 2. Interactive Tables Map & Dashboard
*Monitor live table statuses with color-coded indicators (Green for Available, Red for Occupied, Orange for Reserved).*
<img width="1101" height="892" alt="Screenshot 2026-07-15 113107" src="https://github.com/user-attachments/assets/e7376c87-a039-4807-93a6-a40e77bf8d37" />

### 3. Quick Order Placement
*Select items from the dynamic menu, adjust quantities, and instantly calculate the estimated total.*
<img width="1092" height="866" alt="Screenshot 2026-07-15 113348" src="https://github.com/user-attachments/assets/d947543b-e100-473d-b079-45bb98108eef" />

---

## 🚀 Tech Stack

### Backend
* **Python 3** & **Django 6.x**
* **Django REST Framework (DRF)** — For building clean, stateless RESTful APIs.
* **SimpleJWT** — For secure JSON Web Token (JWT) authentication.
* **PostgreSQL** — Relational database integrated via Docker container.

### Frontend
* **HTML5** & **Vanilla JavaScript (ES6+)** — Using asynchronous `async/await` fetch requests.
* **Tailwind CSS** — For a modern, minimalist, and responsive user interface.
* **FontAwesome Icons** — For visual dashboard elements.

---

## 🛠️ Key Features

* **Secure JWT Authentication:** Waiters must log in to view and manage tables. The system handles session expiration (`401 Unauthorized`) by automatically logging users out to maintain security.
* **Dynamic Table Map:** Table statuses update instantly on the UI:
  * 🟢 **Available:** Ready for new guests or immediate service.
  * 🔴 **Occupied:** Active service; can be cleared using the "Complete Service" action.
  * 🟡 **Reserved:** Guest arrival expected; can be checked in instantly.
* **Streamlined Ordering System:** An interactive modal where waiters can easily select menu items, view live totals, and submit orders directly to the backend.
* **Stateless & CSRF-Free Architecture:** Configured to run entirely on JWT authentication, eliminating session-related CSRF token issues and ensuring a smooth API flow.

---

## 💻 Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/aliyahyayev/restaurant-management-system.git](https://github.com/aliyahyayev/restaurant-management-system.git)
cd restaurant-management-system
