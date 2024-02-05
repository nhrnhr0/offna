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
        const params = {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(record)
        };
        const response = await fetch(url, params);
        const responseData = await response.json();
        return responseData;
    }
}

export class SizesDataFetcher extends DataFetcher {
    constructor() {
        super();
        this.url = '/api/sizes/';
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


export class OptionsDataStore {
    constructor() {
        this.fetcher = null;
        this.options = [];

    }
    // load_options
    async load_options() {
        if (this.fetcher === null || this.fetcher === undefined) {
            throw new Error('Fetcher is not set');
        }
        const data = await this.fetcher.getAll();
        this.options = data;
    }
    // set_fetcher
    /**
     * @param {DataFetcher} fetcher
     * @returns {void}
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
    }
    

    get_options() {
        console.log('get_options', this.options);
        return this.options;
    }

    get_option(id) {
        return this.options.find(option => option.id === id);
    }
    get_option_name(id) {
        console.log('get_option_name', id);
        const option = this.get_option(id);
        return option.name;
    }
}