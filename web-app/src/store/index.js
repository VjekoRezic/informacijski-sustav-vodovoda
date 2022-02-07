import Vue from 'vue'
import Vuex from 'vuex'
import admin from './modules/admin'
import userDashboard from './modules/userDashboard'
import auth from './modules/auth'
import userAccountDetails from './modules/userAccountDetails'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    admin, userDashboard, auth, userAccountDetails
  }
})
