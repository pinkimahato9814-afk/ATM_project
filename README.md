# <mark>**ATM Management System (C++)**<mark>
**Overview**
<img width="953" height="575" alt="image" src="https://github.com/user-attachments/assets/ac433323-9921-4c07-a44a-5f3339d0a587" />


The ATM Management System is a console-based application developed in C++ that simulates real-world ATM operations. It supports both user-level banking operations and administrative controls, with persistent data storage using file handling.

**This project demonstrates concepts of:**

Object-Oriented Programming (OOP)
File Handling
Data Structures
Basic Security Mechanisms (PIN & OTP)
# <mark>**Features**<mark>

    User Features
    Create new account
    Secure login using PIN
    Balance inquiry
    Cash deposit & withdrawal
    Fast cash options
    Fund transfer between users
    PIN change functionality
    Account search and deletion
**Admin Features**
    Secure admin login
    View ATM balance
    Add cash to ATM
    View all user details

# <mark>System Design<mark>
 Technologies Used
      Language: C++
      Libraries:
      <iostream>
      <fstream>
      <ctime>
      <conio.h>
      <windows.h>
# <mark>File Structure<mark>
File Description
UserID.txt	Stores next available user ID
ATM_balance.txt	Stores ATM machine balance
User_details.txt	Stores summary of all users
<userid>.txt	Stores individual user data

# Class Structure
 struct user
  Stores all user-related data:
- User ID
- Name, Age, Address
- Account Type
- PIN
- Balance
- 
  **1.class ATM**

Handles:

      User interface (menus)
      File operations (read/write)
      Transaction processing
      OTP generation
      Receipt printing
**2.class Admin**

    Provides administrative control:
    
    ATM balance management
    User record viewing
    User record maintenance
**3.class User**
    
    Handles user operations:
    Account creation
    Authentication (PIN/OTP)
    Transactions (deposit, withdraw, transfer)
    Account management
# <mark>Program Flow<mark>

  Display welcome screen
  Select role:
  Admin
  User
  Perform respective operations:
  Admin → Manage ATM & users
  User → Perform banking operations
# <mark>Exit system<mark>
Security Features
    4-digit PIN authentication
    OTP verification during account creation
    Hidden PIN input using getch()
    Limited login attempts (3 tries)
**Limitations**
    Stores data in plain text files (not encrypted)
    Platform dependent (Windows-specific libraries)
    Uses goto statements (not recommended in production)
    No database integration
**Basic error handling**
    # <mark>Future Improvements<mark>
        Replace file storage with a database system
        Implement data encryption
        Improve UI (GUI or Web-based interface)
        Remove goto and improve code structure
        Add transaction history logs
        Enhance security mechanisms
🛠️ How to Run



# <mark>Example Operations<mark>
    Create Account → Enter details → OTP → Set PIN
    Withdraw Money → Login → Select amount → Get receipt
    Transfer Money → Enter sender & receiver → Confirm transaction
#  Contributors
    Pragyan Pandey
    Arina Tuladhar
    Uttam Mukhiya
    Pinky Kumari


##<mark> Acknowledgment<mark>

This project was developed as a learning implementation of ATM functionalities using C++ concepts.



