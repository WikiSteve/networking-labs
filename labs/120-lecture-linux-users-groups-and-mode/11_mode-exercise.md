# Mode exercise

1. In the root of the operating system, create a directory called `shares`.
2. Under `/shares`, create directories named `executive`, `managers`, `hr`, `it`, `sales`, and `users`.
3. Change the owners of each directory so it is owned by the appropriate user and group. For `users`, make the ownership `root:users`.
4. Change the permissions for each departmental directory to `rwxrwx---` so that the owner and group can access it but others cannot.
5. For the `users` folder, use permissions `755`.
6. Inside the `users` directory, create another directory called `hr-docs` with full permissions for the owner (the HR manager) and the group (`hr`). Everyone else should have read and execute permissions only.
7. For the `hr` folder, add the sticky bit.

## Solution video

Only view this video **if you're absolutely stuck.**

### 🎥 ugo solution video

[Watch Video](https://www.youtube.com/watch?v=y8vjEFEVj8E)

---
[Prev](10_mode-applying.md) | [Home](README.md) | [Next](12_credits.md)
