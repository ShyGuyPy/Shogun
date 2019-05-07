function start_game(){
    player = new component(50, 50, "red", 10, 120);
    my_game_area.start();
}

var my_game_area = {
    canvas: document.createElement("canvas"),
    start:function() {
        this.canvas.width = 480;
        this.canvas.height = 480;
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
        this.frame_num = 0;
    },
    clear:function() {
        this.context.clearRect(0,0, this.canvas.width, this.canvas.height);
    }
}


