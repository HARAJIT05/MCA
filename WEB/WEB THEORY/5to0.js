async function countdown() {
    for (let i = 5; i >= 0; i--) {
        console.log(i);
        if (i > 0) {
            await new Promise(resolve => setTimeout(resolve, 1000));
        }
    }
}
countdown();