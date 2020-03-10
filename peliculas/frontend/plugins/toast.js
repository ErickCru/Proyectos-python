import Vue from 'vue'
import Toasted from 'vue-toasted';

var options = {
    position: 'top-center',
    duration: 4000,  // milisegundos de vida
}

Vue.use(Toasted, options)