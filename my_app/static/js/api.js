function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -33.8688, lng: 151.2195 },
    zoom: 13
  });
  const card = document.getElementById("pac-card");
  const input = document.getElementById("pac-input");
  map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);
  const autocomplete = new google.maps.places.Autocomplete(input);
  // Bind the map's bounds (viewport) property to the autocomplete object,
  // so that the autocomplete requests use the current map bounds for the
  // bounds option in the request.
  autocomplete.bindTo("bounds", map);
  // Set the data fields to return when the user selects a place.
  autocomplete.setFields(["address_components", "geometry", "icon", "name"]);
  const infowindow = new google.maps.InfoWindow();
  const infowindowContent = document.getElementById("infowindow-content");
  infowindow.setContent(infowindowContent);
  const marker = new google.maps.Marker({
    map,
    anchorPoint: new google.maps.Point(0, -29)
  });
  autocomplete.addListener("place_changed", () => {
    infowindow.close();
    marker.setVisible(false);
    const place = autocomplete.getPlace();

    if (!place.geometry) {
      // User entered the name of a Place that was not suggested and
      // pressed the Enter key, or the Place Details request failed.
      window.alert("No details available for input: '" + place.name + "'");
      return;
    }

    // If the place has a geometry, then present it on a map.
    if (place.geometry.viewport) {
      map.fitBounds(place.geometry.viewport);
    } else {
      map.setCenter(place.geometry.location);
      map.setZoom(17);
    }
    marker.setPosition(place.geometry.location);
    marker.setVisible(true);
    let address = "";

    if (place.address_components) {
      address = [
        (place.address_components[0] &&
          place.address_components[0].short_name) ||
          "",
        (place.address_components[1] &&
          place.address_components[1].short_name) ||
          "",
        (place.address_components[2] &&
          place.address_components[2].short_name) ||
          ""
      ].join(" ");
    }
    infowindowContent.children["place-icon"].src = place.icon;
    infowindowContent.children["place-name"].textContent = place.name;
    infowindowContent.children["place-address"].textContent = address;
    infowindow.open(map, marker);
  });
}












/*


let map;
function initMap() {
  //initialization
  var myLatlng = { lat: -25.363, lng: 131.044 };
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 16,
    center: myLatlng
  });
  infoWindow = new google.maps.InfoWindow;

  //listeners
  /*map.addListener("center_changed", () => {
    // 3 seconds after the center of the map has changed, pan back to the marker.
    window.setTimeout(() => {
      map.panTo(marker.getPosition());
    }, 3000);
  });*/

//////
/*
     // Try HTML5 geolocation.
     if (navigator.geolocation) {
       navigator.geolocation.getCurrentPosition(function(position) {
         myLatlng = {
           lat: position.coords.latitude,
           lng: position.coords.longitude
         };
         infoWindow.setPosition(myLatlng);
         infoWindow.setContent('Location found.');
         infoWindow.open(map);

         map.setCenter(myLatlng);
         const marker = new google.maps.Marker({
           position: myLatlng,
           map,
           title: "Click to zoom"
         });
         marker.addListener("click", () => {
           map.setZoom(8);
           map.setCenter(marker.getPosition());
         });

       }, function() {
         handleLocationError(true, infoWindow, map.getCenter());
       });
     } else {
       // Browser doesn't support Geolocation
       handleLocationError(false, infoWindow, map.getCenter());
     }

     // Set the LocalContextMapView event handlers.
     map.addListener('placedetailsviewshowstart', () => {
       console.log("The 'placedetailsviewshowstart' event just fired!");
     });

     map.addListener('placedetailsviewhidestart', () => {
       console.log("The 'placedetailsviewhidestart' event just fired!");
     });



}



function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                           'Error: The Geolocation service failed.' :
                           'Error: Your browser doesn\'t support geolocation.');
  infoWindow.open(map);
}

function drawCircle(color){//green for >90 //yellow for 90-70 //red for < 70
  const cityCircle = new google.maps.Circle({
   strokeColor: color,
   strokeOpacity: 0.8,
   strokeWeight: 2,
   fillColor: color,
   fillOpacity: 0.35,
   map,
   center: myLatlng,
   radius: 50
  });

}
function checkForPlaceIdInDatabase(placeId){

}

function getPlaces(){

}
*/
