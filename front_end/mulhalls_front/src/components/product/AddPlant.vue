<template>
  <h1 style="color: #181818">New Plant</h1>
<div class="main-container">
  <div class="enter-info">
  <h2 style="color: #181818">Name</h2>
  <input v-model="plant_info.plant_name" placeholder="Name">
  </div>
  <div class="enter-info">
    <h2 style="color: #181818">Type</h2>
    <select v-model="current_type">
      <option v-for="type in plant_type">{{type}}</option>
    </select>
    <div v-if="current_type === 'Tree'" class="enter-info">
      <h2 style="color: #181818">Tree Category</h2>
      <input v-model="tree_sub_info.tree_category" placeholder="Tree Category">
    </div>
    <div v-if="current_type === 'Shrub'" class="enter-info">
      <h2 style="color: #181818">Shrub Category</h2>
      <input v-model="shrub_sub_info.shrub_category" placeholder="Shrub Category">
    </div>
    <div v-if="current_type === 'Perennial'" class="enter-info">
      <h2 style="color: #181818">Perennial Category</h2>
      <input v-model="perennial_sub_info.perennial_category" placeholder="Perennial Category">
      <h2 style="color: #181818">Light Code</h2>
      <input v-model="perennial_sub_info.light_code" placeholder="Light Code">
      <h2 style="color: #181818">Moisture Level</h2>
      <input v-model="perennial_sub_info.moisture_level" placeholder="Moisture Level">
      <h2 style="color: #181818">Care Level</h2>
      <input v-model="perennial_sub_info.care_level" placeholder="Care Level">
    </div>
    <div v-if="current_type === 'Annual'" class="enter-info">
      <h2 style="color: #181818">Annual Category</h2>
      <input v-model="annual_sub_info.annual_category" placeholder="Annual Category">
      <h2 style="color: #181818">Hardy Plant</h2>
      <input type="checkbox" v-model="annual_sub_info.is_hardy" placeholder="Hardy">
      <h2 style="color: #181818">Semi-Hardy Plant</h2>
      <input type="checkbox" v-model="annual_sub_info.is_semi_hardy" placeholder="Semi-Hardy">
      <h2 style="color: #181818">Shade Tolerance</h2>
      <input type="checkbox" v-model="annual_sub_info.shade_tolerant" placeholder="Shade Tolerance">
      <h2 style="color: #181818">Heat Tolerance</h2>
      <input type="checkbox" v-model="annual_sub_info.heat_tolerant" placeholder="Heat Tolerance">
      <h2 style="color: #181818">Drought Tolerance</h2>
      <input type="checkbox" v-model="annual_sub_info.drought_tolerant" placeholder="Drought Tolerance">
    </div>
  </div>
  <div class="enter-info">
    <h2 style="color: #181818">Color</h2>
    <input v-model="plant_info.plant_color" placeholder="Color">
  </div>
  <div class="enter-info">
    <h2 style="color: #181818">Description</h2>
    <input v-model="plant_info.plant_description" placeholder="Description">
  </div>
  <div class="enter-info">
    <h2 style="color: #181818">Size</h2>
    <input v-model="plant_info.plant_size" placeholder="Size">
  </div>
  <div class="enter-info">
    <h2 style="color: #181818">Picture</h2>
    <input type="file" style="color: #181818" @change="inputImage($event)">
  </div>
  <div class="enter-info">
    <h2 style="color: #181818">Department</h2>
    <select v-model="plant_info.department">
      <option v-for="dept in departments"
              :key="dept.department_id"
              :value="dept.department_id">
        {{dept.department_name}}
      </option>
    </select>
  </div>
    <button @click="submitPlant" class="button">Submit</button>
  <div v-if="msg !== ''"><h2 style="color: #181818">{{msg}}</h2></div>
</div>
</template>

<script>
import {mapState} from "vuex";
import {APIService} from "@/http/APIService.js";
import {APIGetPlants} from "@/http/APIService.js";
const apiService = new APIService()
const plantApi = new APIGetPlants()

export default {
  name: "AddPlant",
  data: () => ({
    current_type: "",
    //to change inputs based on plant type
    plant_type: ["Shrub", "Perennial", "Annual", "Tree"],
    //used for api call to add plant
    plant_info: {'plant_type': "",
                 'plant_name': "",
                 'plant_size': "",
                 'plant_color': "",
                 'plant_description': "",
                 'plant_picture': "",
                 'department': ""},
    annual_sub_info: {'annual_category': "",
                      'drought_tolerant': false,
                      'heat_tolerant': false,
                      'is_hardy': false,
                      'is_semi_hardy': false,
                      'plant': "",
                      'shade_tolerant': false,},
    perennial_sub_info: {'care_level': false,
                         'light_code': false,
                         'moisture_level': false,
                         'perennial_category': "",
                         'plant': "",},
    shrub_sub_info: {'plant': "",
                     'shrub_category': "",},
    tree_sub_info: {'plant': "",
                    'tree_category': "",},
    image: "",
    departments: {},
    //used to store any sys messages
    msg: "",
    plant: "",
  }),
  methods: {
    inputImage(event) {
      // This assumes you want to upload the file as soon as it's selected
      this.plant_info.plant_picture = event.target.files[0];
    },
    submitPlant() {
      this.msg = "";
      this.plant_info.plant_type = this.current_type;
      let formData = new FormData();

      formData.append('department', this.plant_info.department);
      formData.append('plant_color', this.plant_info.plant_color);
      formData.append('plant_description', this.plant_info.plant_description);
      formData.append('plant_name', this.plant_info.plant_name);
      formData.append('plant_size', this.plant_info.plant_size);
      formData.append('plant_type', this.plant_info.plant_type);

      if (this.plant_info.plant_picture) {
        formData.append('plant_picture', this.plant_info.plant_picture);
      }
      plantApi.addPlant(formData).then(response => {
        this.plant = response.plant_id;
        switch (this.plant_info.plant_type) {
          case "Annual":
            this.annual_sub_info.plant = this.plant;
            plantApi.addAnnual(this.annual_sub_info).then(response => {
              this.msg = this.plant_info.plant_name + " Added!";
            }).catch(error => {
              console.error("uh oh: ", error)
              this.msg = "Error, Try again!";
            })
            break;
          case "Perennial":
            this.perennial_sub_info.plant = this.plant;
            plantApi.addPerennial(this.perennial_sub_info).then(response => {
              this.msg = this.plant_info.plant_name + " Added!";
            }).catch(error => {
              console.error("uh oh: ", error)
              this.msg = "Error, Try again!";
            })
            break;
          case "Tree":
            this.tree_sub_info.plant = this.plant;
            plantApi.addTree(this.tree_sub_info).then(response => {
              this.msg = this.plant_info.plant_name + " Added!";
            }).catch(error => {
              console.error("uh oh: ", error)
              this.msg = "Error, Try again!";
            })
            break;
          case "Shrub":
            this.shrub_sub_info.plant = this.plant;
            plantApi.addShrub(this.shrub_sub_info).then(response => {
              this.msg = this.plant_info.plant_name + " Added!";
            }).catch(error => {
              console.error("uh oh: ", error)
              this.msg = "Error, Try again!";
            })
            break;
        }
        this.current_type = "";
        this.image = ""
        this.plant_info = {'plant_type': "",
                           'plant_name': "",
                           'plant_size': "",
                           'plant_color': "",
                           'plant_description': "",
                           'plant_picture': "",
                           'department': ""}
        this.plant_sub_info = {};
        this.msg = "Plant Added!";
        }).catch(error => {
        console.error('Error:', error);
        this.msg = "Plant not added."
      });
    },
    async getDepartments() {
      //list all questions in db
      const result = await apiService.getDepartments();
      this.departments = result.data;
    }
  },
  computed: {
    ...mapState({
      isLoggedIn: state => state.isLoggedIn,
      isEmpl: state => state.isEmpl,
      email: state => state.email,
      username: state => state.username,
      loading: state => state.loading,
      account_info: state => state.account_info,
    }),
  },
  mounted() {
    this.getDepartments();
  },
}
</script>

<style scoped>

</style>