function fetchUserData() {
    return new Promise((resolve) => {
        setTimeout(() => {
            const userInfo = {
                id: 1,
                name: "Arthur Morgan",
                email: "arthur.morgan@blackwater.com"
            };
            resolve(userInfo);
        }, 3000);
    });
}
fetchUserData().then((user) => {
    console.log("User data fetched:", user);
});