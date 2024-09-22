# Chat Application

## Project Overview
This is a **real-time chat application** built for **CPSC 362: Foundations of Software Engineering**. The goal of this project is to help users communicate with each other through private or group chats in real-time. Users can create profiles, join chat rooms, and send messages instantly.

## Features
- **Real-time Messaging**: Send and receive messages instantly.
- **Chat Rooms**: Join public or private chat rooms to communicate with others.
- **User Profiles**: Create a profile with a username and avatar.
- **(Optional)** **Group Chats**: Create and join group chats with multiple users.
- **(Optional)** **File Sharing**: Share files such as images and documents.

## Requirements

### Functional Requirements
1. **Messaging**:
   - Users must be able to send and receive messages in real time.
   - Example: "The message should appear immediately in the chat window."
  
2. **User Profiles**:
   - Users must be able to create and update their profiles.
   - Example: "A user can upload an avatar and set a username."

3. **Chat Rooms**:
   - Users can join and leave chat rooms.
   - Example: "Users can select a chat room from the list and participate."

### Non-Functional Requirements
1. **Performance**:
   - Messages should be sent and received instantly, with no noticeable delay.
  
2. **Scalability**:
   - The system should be able to handle up to 1,000 users at once without slowing down.
  
3. **Security**:
   - User data, including messages, must be encrypted and securely stored.

## Use Case Diagram
(Include an image of your **Use Case Diagram** here.)

This diagram shows the basic interactions between users and the system, such as logging in, joining chat rooms, and sending messages.

## Context Diagram
(Include an image of your **Context Diagram** here.)

This diagram shows how the chat system interacts with external components like the server and database.

## Installation Instructions
To run the chat application on your computer:
1. Download the project:
    ```bash
    git clone https://github.com/your-repo-url.git
    ```
2. Open the project folder:
    ```bash
    cd your-project-folder
    ```
3. Install the required software:
    ```bash
    npm install
    ```
4. Run the application:
    ```bash
    npm start
    ```

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Node.js, Express
- **Database**: MongoDB
- **Real-time Communication**: Socket.io

## Contributors

## License
This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
