let map;
var myLatlng = {lat:42.0420249 , lng:-87.8863285};//defualt pos
function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: myLatlng,
    zoom: 18.5
  });
  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      myLatlng = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
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

    }, function() {});
  } else {
    // Browser doesn't support Geolocation
    map.setCenter(myLatlng);
  }


  const card = document.getElementById("pac-card");
  const input = document.getElementById("pac-input");
  map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);
  const autocomplete = new google.maps.places.Autocomplete(input);

  autocomplete.bindTo("bounds", map);
  // Set the data fields to return when the user selects a place.
  autocomplete.setFields(["address_components", "geometry", "name", "place_id"]);
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
    infowindowContent.children["place-name"].textContent = place.name;
    infowindowContent.children["place-address"].textContent = address;
    console.log(place.place_id);
    console.log(place.name);
    console.log(address)
    console.log(checkForPlaceIdInDatabase({'id': place.place_id, 'name': place.name}));

    infowindow.open(map, marker);
  });
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

function checkForPlaceIdInDatabase2(placeId) {
  //$.post("/api", {id: placeId});
  // $.post({
  //   type : 'POST',
  //   url : "api",
  //   contentType: 'application/json;charset=UTF-8',
  //   data : {'b_id' :placeId}
  // });
  // $.post("api", {"place_id" : placeId}, function(){
	// });

  //event.preventDefault();
}

// function updateRightSide(){}
// function checkForPlaceIdInDatabase2(placeId){
//   var xhttp = new XMLHttpRequest();
//
//   xhttp.open( "GET", "/api?place_id="+placeId, true ); // false for synchronous request
//   xhttp.send( null );
//   return xhttp.responseText;
//ChIJ4fpH7c1fBYgRWFd77Dfo2wA
  //xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  //xhttp.setRequestHeader("id", placeId, false);
  // xhttp.onreadystatechange = function() {
  //    if (this.readyState == 4 && this.status == 200) {
  //
  //       // Response
  //       return response = this.responseText;
  //
  //    }
  // };
  // xhttp.open("GET", "localhost:5000/api?id=" + placeId, true);
  // xhttp.send()
  // xhttp.send("?id="+placeId);
//}

function checkForPlaceIdInDatabase(place) {
  var req = new XMLHttpRequest();
  var result = document.getElementById('result');
  req.onreadystatechange = function()
  {
    if(this.readyState == 4 && this.status == 200) {
      result.innerHTML = this.responseText;
    } else {
      result.innerHTML = "No business was chosen";
    }
  }

  req.open('POST', '/api', true);
  req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
  req.send("name=" + place.name+'.'+place.id);
}
