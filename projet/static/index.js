document.addEventListener("DOMContentLoaded", function() {
    let matricule = document.getElementById('matricule');
    let marque = document.getElementById('marque');
    let kilometrage = document.getElementById('kilometrage');
    let prixJours = document.getElementById('prix_jours');
    let disponibilite = document.getElementsByName('disponibilite');
    let cre = document.getElementById('cre');
    let searchBar = document.getElementById('search-bar');
    let carTableBody = document.getElementById('car-table-body');
    let deleteAllBtn = document.getElementById('delete-all');
    let errorMessage = document.getElementById('error-message');

    let mood = 'create';
    let currentIndex;

    let cars = localStorage.cars ? JSON.parse(localStorage.cars) : [];

    cre.onclick = function() {
        if (verifier()) {
            let dispo;
            for (let i = 0; i < disponibilite.length; i++) {
                if (disponibilite[i].checked) {
                    dispo = disponibilite[i].value;
                    break;
                }
            }

            let newCar = {
                matricule: matricule.value,
                marque: marque.value,
                kilometrage: parseFloat(kilometrage.value),
                prixJours: parseFloat(prixJours.value),
                disponibilite: dispo
            };

            if (mood === 'create') {
                cars.push(newCar);
            } else {
                cars[currentIndex] = newCar;
                mood = 'create';
                cre.innerHTML = 'Create';
            }

            localStorage.setItem('cars', JSON.stringify(cars));
            clearInputs();
            showdata();
        }
    };

    function verifier() {
        if (matricule.value === '' || marque.value === '' || kilometrage.value === '' || prixJours.value === '') {
            errorMessage.innerHTML = 'Tous les champs sont obligatoires.';
            errorMessage.style.display = 'block';
            return false;
        } else if (kilometrage.value < 0 || prixJours.value < 0) {
            errorMessage.innerHTML = 'Le kilométrage et le prix par jour doivent être non-négatifs.';
            errorMessage.style.display = 'block';
            return false;
        } else {
            errorMessage.style.display = 'none';
            return true;
        }
    }

    function clearInputs() {
        matricule.value = '';
        marque.value = '';
        kilometrage.value = '';
        prixJours.value = '';
        for (let i = 0; i < disponibilite.length; i++) {
            disponibilite[i].checked = false;
        }
        disponibilite[0].checked = true; // Default to "louer"
    }

    function showdata() {
        let tab = '';
        for (let i = 0; i < cars.length; i++) {
            tab += `
            <tr>
                <td>${i + 1}</td>
                <td>${cars[i].matricule}</td>
                <td>${cars[i].marque}</td>
                <td>${cars[i].kilometrage}</td>
                <td>${cars[i].prixJours}</td>
                <td>${cars[i].disponibilite}</td>
                <td class="car-buttons">
                    <button onclick="updateCar(${i})">Update</button>
                    <button onclick="deleteCar(${i})">Delete</button>
                </td>
            </tr>`;
        }
        carTableBody.innerHTML = tab;

        if (cars.length > 0) {
            deleteAllBtn.innerHTML = `<button onclick="deleteAll()">Delete All (${cars.length})</button>`;
        } else {
            deleteAllBtn.innerHTML = '';
        }
    }

    window.deleteCar = function(index) {
        cars.splice(index, 1);
        localStorage.setItem('cars', JSON.stringify(cars));
        showdata();
    };

    window.deleteAll = function() {
        localStorage.clear();
        cars = [];
        showdata();
    };

    window.updateCar = function(index) {
        matricule.value = cars[index].matricule;
        marque.value = cars[index].marque;
        kilometrage.value = cars[index].kilometrage;
        prixJours.value = cars[index].prixJours;
        for (let i = 0; i < disponibilite.length; i++) {
            if (disponibilite[i].value === cars[index].disponibilite) {
                disponibilite[i].checked = true;
            }
        }

        mood = 'update';
        cre.innerHTML = 'Modify';
        currentIndex = index;
    };

    let searchMode = 'matricule';

    window.setSearchMode = function(mode) {
        searchMode = mode;
        searchBar.value = '';
        showdata();
    };

    window.searchData = function(value) {
        let filteredCars = cars.filter(car => {
            if (searchMode === 'matricule') {
                return car.matricule.includes(value);
            } else {
                return car.marque.includes(value);
            }
        });

        let tab = '';
        for (let i = 0; i < filteredCars.length; i++) {
            tab += `
            <tr>
                <td>${i + 1}</td>
                <td>${filteredCars[i].matricule}</td>
                <td>${filteredCars[i].marque}</td>
                <td>${filteredCars[i].kilometrage}</td>
                <td>${filteredCars[i].prixJours}</td>
                <td>${filteredCars[i].disponibilite}</td>
                <td class="car-buttons">
                    <button onclick="updateCar(${i})">Update</button>
                    <button onclick="deleteCar(${i})">Delete</button>
                </td>
            </tr>`;
        }
        carTableBody.innerHTML = tab;
    }

    searchBar.oninput = function() {
        searchData(searchBar.value);
    };

    showdata();
});
