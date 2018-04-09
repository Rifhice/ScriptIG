#!/bin/bash
curl -H "Content-Type: application/json" -X POST -d '{"prenom":"'$1'","email":"'$2'","nom":"'$3'","password1":"'$4'","password2":"'$4'","section":"GBA","annee":5}' http://www.dolcevitech.fr/api/auth/signup
