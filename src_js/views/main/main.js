export function vt() {
    return ['span', `counter: ${r.get('remote', 'adapter', 'counter')}`];
}
