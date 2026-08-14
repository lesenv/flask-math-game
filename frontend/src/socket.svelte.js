// src/socket.svelte.js
import { io } from "socket.io-client";

class SocketState {
    socket = $state(io.prototype);

    connect() {
        if (this.socket) return this.socket;

        this.socket = io();
        return this.socket;
    }

    disconnect() {
        this.socket?.disconnect();
        this.socket = null;
    }

    joinRoom(username, roomname) {
        this.socket?.emit("join", { username, roomname });
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

    sidebar_tasks() {
        this.socket?.emit("get_sidebar_tasks", {});
    }

    checks() {
        this.socket?.emit("get_checks", {});
    }
}

export const socketState = new SocketState();