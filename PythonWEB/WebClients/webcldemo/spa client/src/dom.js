export const findParent = (node, tagName) => {
    if (!node) return null;

    tagName = tagName.toUpperCase()
    if (node.parentElement && node.parentElement.tagName === tagName) {
        return node.parentElement
    } else {
        return findParent(node.parentElement, tagName)
    }
}

export const formValuesToObject = (formValues) => {
    return Array.from(formValues.entries())
        .reduce((prev, [name, value]) => ({ ...prev, [name]: value }), {})
}