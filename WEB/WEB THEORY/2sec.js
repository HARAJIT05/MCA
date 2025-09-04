async function Hello() {
    await new Promise(resolve => setTimeout(resolve, 2000));
    console.log("Hello, Welcome to JavaScript!");
}
Hello();