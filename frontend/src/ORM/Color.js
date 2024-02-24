import { BACKEND_URL } from "$lib/config";
import { sendJsonRequest } from "../network/fetcher";
class ORM_Object {
    /**
     * 
     * @param {string|undefined} id 
     */
    constructor(id) {
        this.id = id;
    }

    async save() {
        if(this.id) {
            // update
            return await this.update();
        }else {
            // create
            return await this.create();
        }
    }

    /**
     * @returns {Promise<Response>}
     */
    async create() {
        new Error("Not implemented");
        return new Promise((resolve, reject) => {
            resolve(new Response());
        });
    }
    /**
     * @returns {Promise<Response>}
     */
    async update() {
        new Error("Not implemented");
        return new Promise((resolve, reject) => {
            resolve(new Response());
        });
    }

    /**
     * @returns {Object}
     */
    toJson() {
        new Error("Not implemented");
        return {};
    }
}


export class Color extends ORM_Object {

    /**
     * 
     * @param {string|undefined} id 
     * @param {string|undefined} name 
     * @param {string|undefined} color 
     * @param {number|undefined} order 
     */
    constructor(id, name,color, order) {
        super(id);
        this.name = name;
        this.color = color;
        this.order = order;
    }

    /**
     * @returns {Promise<Color>}
     */
    static async get(id) {
        const response = await fetch(`${BACKEND_URL}/api/colors/${id}/`);
        const data = await response.json();
        return new Color(data.id, data.name, data.color, data.order);
    }
    
    /**
     * @returns {Promise<Response>}
     */
    async create() {
        const response = await sendJsonRequest(`${BACKEND_URL}/api/colors/`, 'POST', JSON.stringify(this.toJson()));
        return response;
    }

    /**
     * @returns {Promise<Response>}
    */
    async update() {
        const response = await sendJsonRequest(`${BACKEND_URL}/api/colors/${this.id}/`, 'PUT', JSON.stringify(this.toJson()));
        return response;
    }

    /**
     * @returns {Object}
     */
    toJson() {
        return {
            name: this.name,
            color: this.color,
            order: this.order
        };
    }






}