#!/usr/bin/node
class Rectangle {
    constructor(w, h){
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }

    print()
    {
        for (let index = 0; index < this.height; index++) {
            console.log('X'.repeat(this.width, 10))
        }
    }

    double()
    {
        for (let index = 0; index < this.height * 2; index++) {
            console.log('X'.repeat(this.width * 2, 10))
        }
    }

    rotate()
    {
        for (let index = 0; index < this.width; index++) {
            console.log('X'.repeat(this.height, 10))
        }
    }
}

module.exports = Rectangle;
