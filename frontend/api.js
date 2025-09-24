// ...existing code...
const BASE_URL = "http://127.0.0.1:5000";

async function request(url, opts = {}) {
    opts = Object.assign({}, opts);
    opts.headers = Object.assign({}, opts.headers || {});
    // nếu gửi FormData thì không set Content-Type
    if (!(opts.body instanceof FormData) && !opts.headers["Content-Type"]) {
        opts.headers["Content-Type"] = "application/json";
    }
    if (opts.body && !(opts.body instanceof FormData) && typeof opts.body !== "string") {
        opts.body = JSON.stringify(opts.body);
    }
    const res = await fetch(url, opts);
    if (!res.ok) {
        const txt = await res.text();
        throw new Error(txt || res.statusText);
    }
    try {
        return await res.json();
    } catch {
        return null;
    }
}

export async function getCategories() {
    return request(`${BASE_URL}/api/categories`);
}

export async function addCategoryJSON(payload) {
    return request(`${BASE_URL}/api/categories`, {
        method: "POST",
        body: payload
    });
}

export async function deleteCategory(name) {
    return request(`${BASE_URL}/api/categories`, {
        method: "DELETE",
        body: { name }
    });
}

export async function createOrderJSON(payload) {
    return request(`${BASE_URL}/api/orders`, {
        method: "POST",
        body: payload
    });
}

export async function getOrders() {
    return request(`${BASE_URL}/api/orders`);
}
// ...existing code...