<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My account</h1>
            </div>

            <div class="column is-12">
                <div class="field">
                    <label>First Name</label>
                    <div class="control">
                        <input type="text" class="input" :value="user.first_name" disabled>
                    </div>
                </div>

                <div class="field">
                    <label>Last Name</label>
                    <div class="control">
                        <input type="text" class="input" :value="user.last_name" disabled>
                    </div>
                </div>

                <div class="field">
                    <label>Email adress:</label>
                    <div class="control">
                        <input type="text" class="input" :value="user.username" disabled>
                    </div>
                </div>

                <div class="buttons">
                    <router-link :to="{ name: 'EditMember', params: { id: $store.state.user.id }}" class="button is-light">Edit</router-link>

                    <button @click="logout()" class="button is-danger">Log out</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import { toast } from 'bulma-toast'
    export default {
        name: 'MyAccount',
        data() {
            return {
                user: {}
            }
        },
        mounted() {
            this.getUser()
        },
        methods: {
            async logout() {
                await axios
                    .post('/api/v1/token/logout/')
                    .then(response => {
                        console.log('Logged out')
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
                
                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')
                localStorage.removeItem('username')
                localStorage.removeItem('userid')
                localStorage.removeItem('team_name')
                localStorage.removeItem('team_id')
                this.$store.commit('removeToken')

                this.$router.push('/')
            },

            async getUser() {
                this.$store.commit('setIsLoading', true)

                const userID = this.$route.params.id

                await axios
                    .get(`/api/v1/teams/member/${userID}/`)
                    .then(response => {
                        this.user = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            },
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                const userID = this.$route.params.id

                await axios
                    .put(`/api/v1/teams/member/${userID}/`, this.user)
                    .then(response => {
                        toast({
                            message: 'The user was updated',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$router.push({ name: 'MyAccount' })
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }

        }
    }
</script>