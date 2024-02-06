import { writable } from 'svelte/store';
import { get } from 'svelte/store';
export class DataFetcher {
    constructor() {
        this.baseUrl = 'http://127.0.0.1:8000';
        this.url = '';
    }

    async getData(params) {
        const url = this.baseUrl + this.url + '?' + new URLSearchParams(params);
        

        const response = await fetch(url);
        const data = await response.json();
        
        return data;
    }

    async getAll() {
        const data = await this.getData();
        return data;
    }
    async update_record(id, record) {
        console.log('update_record', id, record);
        const url = this.baseUrl + this.url + id + '/';

        const formData = new FormData();
        debugger;
        for (const key in record) {
            if (record.hasOwnProperty(key)) {
                const value = record[key];
                // if it's an array, we need to loop through it and append each value
                if (Array.isArray(value)) {
                    for (const val of value) {
                        formData.append(key, val);
                    }
                } else {
                    formData.append(key, value);
                }
            }
        }

        const params = {
            method: 'PUT',
            headers: {
                // 'Content-Type': 'application/json'
            },
            body: formData,
        };
        const response = await fetch(url, params);
        const responseData = await response.json();
        return responseData;
    }

    // async update_image(id, file, key) {
    //     const url = this.baseUrl + this.url + id + '/' + key + '/';

        
    //     const formData = new FormData();
    //     formData.append(key, file);

    //     const params = {
    //         method: 'PUT',
    //         body: formData,
    //     };
    //     const response = await fetch(url, params);
    //     const responseData = await response.json();
    //     debugger;
    //     return responseData;
    
    // }
}

export class SizesDataFetcher extends DataFetcher {
    constructor() {
        super();
        this.url = '/api/sizes/';
    }
}

export class CategoriesDataFetcher extends DataFetcher {
    constructor() {
        super();
        this.url = '/api/categories/';
    }
}


export class SizesGroupsDataFetcher extends DataFetcher{
    constructor() {
        super();
        this.url = '/api/sizes_groups/';
    }
}


export class ColorsDataFetcher extends DataFetcher { 
    constructor() {
        super();
        this.url = '/api/colors/';
    }
}

export class ProductsDataFetcher extends DataFetcher {
    constructor() {
        super();
        this.url = '/api/products/';
    }
}

export class OptionsDataStore {
    id_field = 'id';
    label_field = 'name';
    /**
     * @type {DataFetcher | null}
     */
    fetcher = null;
    /**
     * @type {Array<Object>}
     */
    options = [];

    ids_labels_array = [];

    /**
     * 
     * @param {string} id_field 
     * @param {string} label_field 
     */
    constructor(id_field, label_field, fetcher=null) {
        if (id_field) {
        this.id_field = id_field;
        }
        if(label_field) {
        this.label_field = label_field;
        }
        this.fetcher = fetcher;
    }
    // load_options
    async load_options() {
        if (this.fetcher === null || this.fetcher === undefined) {
            throw new Error('Fetcher is not set');
        }
        const data = await this.fetcher.getAll();
        this.options = data;

        this.ids_labels_array = this.options.map((option) => {
            return {
                id: option[this.id_field],
                label: option[this.label_field]
            };
        });
        return this;
    }
    // set_fetcher
    /**
     * @param {DataFetcher} fetcher
     * @returns {OptionsDataStore}
     * @throws {Error}
     * @memberof OptionsDataStore
     * @description
     * Sets the fetcher to be used by the data store
     * @example
     * const fetcher = new SizesDataFetcher();
     * const store = new OptionsDataStore();
     * store.set_fetcher(fetcher);
     * await store.load_options();
     */
    set_fetcher(fetcher) {
        this.fetcher = fetcher;
        return this;
    }
    

    get_raw_data() {
        console.log('get_options', this.options);
        return this.options;
    }

    get_options() {
        return this.ids_labels_array;
    }



}