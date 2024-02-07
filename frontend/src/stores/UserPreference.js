import { browser } from '$app/environment'
import { writable } from 'svelte/store'


function create_localstore_writable(key, startValue) {
    debugger;
    const json = browser && localStorage.getItem(key) || null
  const { subscribe, set, update } = writable(json ? JSON.parse(json) : startValue)
    // is array and length > 0
    subscribe(current => {
        browser && current !== undefined && current !== null && localStorage
            .setItem(key, JSON.stringify(current))
    })

    return {
        subscribe,
        set,
        update
    }
}

export const userPreferenceProductsTable = create_localstore_writable('user-preference-products-table', [])
export const userPreferenceSizesTable = create_localstore_writable('user-preference-sizes-table', [])
export const userPreferenceSizesGroupsTable = create_localstore_writable('user-preference-sizes-group-table', [])
export const userPreferenceColorsTable = create_localstore_writable('user-preference-colors-table', [])
export const userPreferenceCategoriesTable = create_localstore_writable('user-preference-categories-table', [])
