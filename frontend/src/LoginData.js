export class LoginData {
    static STORAGE_KEY = 'login';

    static getAll() {
        return JSON.parse(localStorage.getItem(this.STORAGE_KEY)) ?? {};
    }

    static get(name) {
        return this.getAll()[name] ?? [];
    }

    static set(name, value) {
        const data = this.getAll();
        data[name] = value;
        this.save(data);
    }

    static delete(name) {
        const data = this.getAll();
        delete data[name];
        this.save(data);
    }

    static getUsers() {
        return Object.keys(this.getAll());
    }

    static save(data) {
        localStorage.setItem(
            this.STORAGE_KEY,
            JSON.stringify(data)
        );
    }
}