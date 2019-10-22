class Room {
    constructor(name, description, id=0, x=null, y=null) {
        this.id = id
        this.name = name
        this.description = description
        this.n_to = None
        this.s_to = None
        this.e_to = None
        this.w_to = None
        this.x = x
        this.y = y
    }
}