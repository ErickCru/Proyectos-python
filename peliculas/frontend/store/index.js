export const state = () => ({
    token: null,
    user: null,
    favIds: []
})

export const mutations = {
    saveUser(state, user) {
        state.user = user;
    },
    saveToken(state, token) {
        state.token = token;
    },
    toggleFavorite(state, id) {
        if (id != null) {
            var index = state.favIds.indexOf(id)
            if (index !== -1) state.favIds.splice(index, 1)
            else state.favIds.push(id)
        }
        else
            state.favIds = []
    }
}