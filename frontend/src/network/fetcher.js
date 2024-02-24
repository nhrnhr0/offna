


/**
 * 
 * @param {string} url 
 * @param {"GET"|"POST"|"PUT"|"DELETE"} method
 * @param {string|undefined} body 
 * @returns Promise<Response>
 */
export async function sendJsonRequest(url, method, body=undefined) {
    const response = await fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: body
    });
    return response;
}

/**
 * 
 * @param {string} url 
 * @param {"GET"|"POST"|"PUT"|"DELETE"} method
 * @param {FormData} body
 * @returns Promise<Response>
 */
export async function sendFormDataRequest(url, method, body) {
    const response = await fetch(url, {
        method: method,
        body: body
    });
    return response;
}