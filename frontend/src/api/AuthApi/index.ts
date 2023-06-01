import { LoginAPIInstance, DefaultAPIInstance } from "@/api/index";

export const AuthApi = {
  login(email, password) {
    const url = '/auth/token/login/';
    const data = { username: email, password };
    return LoginAPIInstance.post(url, data);

  },
  register(email, password) {
    const url = '/auth/users/';
    const data = { email, password };
    return DefaultAPIInstance.post(url, data);
  },
  logout() {
    const url = '/auth/token/logout/';
    return DefaultAPIInstance.post(url, {});
  }
}