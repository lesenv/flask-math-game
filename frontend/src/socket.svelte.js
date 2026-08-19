// src/socket.svelte.js
import { io } from "socket.io-client";

class SocketState {
	socket = $state(null);

	connect() {
		if (this.socket) return this.socket;

		this.socket = io({
            withCredentials: true
        });
		return this.socket;
	}

	disconnect() {
		this.socket?.disconnect();
		this.socket = null;
	}

	joinRoom(username, roomname, tasktype) {
		this.socket?.emit("join", { username, roomname, tasktype });
	}

	leaveRoom() {
		this.socket?.emit("leave", {});
	}

    submitResults(result) {
        this.socket?.emit("solve", { c: result });
    }

    submitMessage(message) {
        this.socket?.emit("send_message", { message });
    }

    updateTasks(enabled_tasks) {
        this.socket?.emit("tasks_state", { enabled_tasks }); 
    }
}

export const socketState = new SocketState();