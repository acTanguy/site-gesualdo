$('#comment_measure').keyup(function() {$('#comment_measure').val(this.value.match(/[0-9]*/));});

        $(function()
            {
                $("#addCom").hide();
                /*
                    Validation des messages :
                        Un message à valider comporte un formulaire qui comporte la classe "validateCom". En validant ce formulaire, on demande au serveur d'enregistrer le changement.
                        Si la réponse est positive (la réponse doit être l'id du message validé), alors on notifie le changement en rétablissant l'opacité de la zone du message.
                */
                $('form[class="validateCom"]').submit( function() {
                    var url = $(this).attr('action');
                    $.ajax({
                        type: "POST",
                        url: url,
                        data: $(this).serializeArray(),
                        success: function(data) {
                            if(data != "-1")
                            {
                                $("#comment" + data).css("opacity", 1);
                                $("#valide" + data).fadeOut();
                            }
                        }
                    });
                    return false;
                });
                
                
                /*
                    Suppression des messages :
                        Pour supprimer un message, on demande via un formulaire de classe "deletCom". Celui-ci comporte l'id du message à supprimer.
                        Si la réponse est positive (la réponse doit être l'id du message supprimé), alors on notifie le changement en cachant la zone du message.
                */
                $('form[class="deletCom"]').submit( function() {
                    var url = $(this).attr('action');
                    $.ajax({
                        type: "POST",
                        url: url,
                        data: $(this).serializeArray(),
                        success: function(data) {
                            if(data != -1)
                            {
                                $("#comment" + data).fadeOut();
                            }
                        }
                    });
                    return false;
                });
                
                $('form[class="archiveCom"]').submit( function() {
                    var url = $(this).attr('action');
                    $.ajax({
                        type: "POST",
                        url: url,
                        data: $(this).serializeArray(),
                        success: function(data) {
                            if(data != -1)
                            {
                                $("#comment" + data).fadeOut();
                            }
                        }
                    });
                    return false;
                });
                
                /*
                    Ajout de messages :
                        Pour ajouter un message, on demande via un formulaire d'id "ajoutCom", qui comporte le numéro de la mesure et le message.
                        En cas d'insertion réussie, on crée une zone pour le message, qui comporte le nom du posteur, les boutons et formulaires pour valider ou supprimer
                        si l'utilisateur en a les droits, puis le message.
                */
                $("#addCom").submit( function() {
                    if($("#comment_text").val() == "")
                        return false;
                    var url = $(this).attr('action');
                    var formData = new FormData($(this)[0]);
                    $.ajax({
                        type: "POST",
                        url: url,
                        data: formData,
                        processData: false,
                        contentType: false,
                        success: function(data) {
                            var zone = $("#piece_comments_zone");
                            var divCom = $("<div id='comment" + data + "' class='piece_comment_text comment_invalide'></div>");
                            var table = $('<table></table>');
                            var tete = $('<thead></thead>');
                            var pseudo = $('<th></th>');
                            pseudo.appendTo(tete);
                            
                            {% if user.is_authenticated %} // S'il est authentifié, alors il possède un compte, qui possède un nom bref.
                                pseudo.text("{{ user.userprofile.person.nickname }}");
                            {% else %}
                                pseudo.text("Visitor"); // Sans quoi, il est considéré comme un internaute.
                            {% endif %}
                            
                            {% if perms.gesualdo.validate_message %} // Si l'utilisateur possède le droit de valider les messages, on lui offre la possibilité
                            
                                var validations = $('<th></th>');
                                validations.appendTo(tete);
                                
                                var formValide = $('<form class="validateCom" method="POST"></form>');
                                formValide.attr('action', "{% url 'messageprocessing:validateComment' %}");
                                formValide.html("{% csrf_token %}");
                                var valide = $('<input id="valide' + data + '" type="image" class="commit_message_button" title="Validate" alt="V" value="submit"/>');
                                valide.attr('src', '{% static "imagesCss/valider.gif" %}');
                                var hiddenValide = $('<input type="hidden" name="id" value="' + data + '"/>');
                                valide.appendTo(formValide);
                                hiddenValide.appendTo(formValide);
                                formValide.appendTo(validations);
                                
                                var formArchive = $('<form class="archiveCom" method="POST"></form>');
                                formArchive.attr('action', "{% url 'messageprocessing:archiveComment' %}");
                                formArchive.html("{% csrf_token %}");
                                var archive = $('<input id="archive' + data + '" type="image" class="commit_message_button" title="Validate" alt="A" value="submit"/>');
                                archive.attr('src', '{% static "imagesCss/archive.png" %}');
                                var hiddenArchive = $('<input type="hidden" name="id" value="' + data + '"/>');
                                archive.appendTo(formArchive);
                                hiddenArchive.appendTo(formArchive);
                                formArchive.appendTo(validations);
                                
                                var formInvalide = $('<form class="deletCom" method="POST"></form>');
                                formInvalide.attr('action', "{% url 'messageprocessing:supprimerComment' %}");
                                formInvalide.html("{% csrf_token %}");
                                var invalide = $('<input id="suppr' + data + '" type="image" class="commit_message_button" title="Delete" alt="X" value="submit"/>');
                                invalide.attr('src', '{% static "imagesCss/refuser.png" %}');
                                var hiddenInvalide = $('<input type="hidden" name="id" value="' + data + '"/>');
                                invalide.appendTo(formInvalide);
                                hiddenInvalide.appendTo(formInvalide);
                                formInvalide.appendTo(validations);
                                
                                // On change le comportement des formulaires, comme pour ceux qui ont été généré à la création de la page.
                                formValide.submit( function() {
                                    var url = $(this).attr('action');
                                    $.ajax({
                                        type: "POST",
                                        url: url,
                                        data: $(this).serializeArray(),
                                        success: function(data2) {
                                            if(data2 != "-1")
                                            {
                                                $("#comment" + data2).css("opacity", 1);
                                                $("#valide" + data2).fadeOut();
                                            }
                                        }
                                    });
                                    return false;
                                });
                                
                                formArchive.submit( function() {
                                    var url = $(this).attr('action');
                                    $.ajax({
                                        type: "POST",
                                        url: url,
                                        data: $(this).serializeArray(),
                                        success: function(data2) {
                                            if(data2 != "-1")
                                            {
                                                $("#comment" + data2).fadeOut();
                                            }
                                        }
                                    });
                                    return false;
                                });
                                
                                formInvalide.submit( function() {
                                    var url = $(this).attr('action');
                                    $.ajax({
                                        type: "POST",
                                        url: url,
                                        data: $(this).serializeArray(),
                                        success: function(data2) {
                                            if(data2 != -1)
                                            {
                                                $("#comment" + data2).fadeOut();
                                            }
                                        }
                                    });
                                    return false;
                                });
                                
                            {% endif %}
                            
                            var tr = $('<tr></tr>');
                            var td = $('<td></td>');
                            td.text($('#comment_text').val());
                            {% if perms.gesualdo.validate_message %}
                                td.attr('colspan', '2');
                            {% endif %}

                            
                            td.appendTo(tr);
                            tete.appendTo(table);
                            tr.appendTo(table);
                            table.appendTo(divCom);
                            divCom.prependTo(zone);
                            divCom.fadeOut();
                            divCom.fadeIn();
                            $('#comment_measure').val("");
                            $('#comment_text').val("");
                        }
                    });
                    return false;
                });
                
                
            }
        );
        
        
        
        function deletComment(id)
        {
            var http = getXMLHttpRequest();
            var data = "id=" + id;
            http.open("POST", "{% url 'messageprocessing:refuseComment' %}", true);
            http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            http.setRequestHeader("Content-length", data.length);
            http.onreadystatechange = function() {
                if(http.readyState == 4)
                {
                    var com = $("#comment" + id);
                    com.fadeOut();
                }
            }
            http.send(data);
        }
        
        function validerComment(id)
        {
            var http = getXMLHttpRequest();
            var data = "id=" + id;
            http.open("POST", "{% url 'messageprocessing:validateComment'%}", true);
            http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            http.setRequestHeader("Content-length", data.length);
            http.onreadystatechange = function() {
                if(http.readyState == 4)
                {
                    var com = $("#comment" + id);
                    com.css("opacity", 1);
                }
            }
            http.send(data);
        }
        
        
        
        function ajouteComment()
        {
            var http = getXMLHttpRequest();
            var message = document.getElementById("comment_measure").value;
            var mesure = document.getElementById("comment_text").value;
            var data = "message=" + encodeURIComponent(unescape(message)) + "&piece=" + encodeURIComponent(unescape({{ piece.id }})) + "&mesure=" + encodeURIComponent(unescape(mesure));
            alert(data);
            
            http.open("POST", "{% url 'messageprocessing:addComment'%}", true);
            http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            http.setRequestHeader("Content-length", data.length);
            http.onreadystatechange = function() {
                if(http.readyState == 4)
                {
                    alert(http.responseText);
                }
            }
            
            http.send(data);
        }
        
        function triggerComment()
        {
            $("#buttonCom").hide();
            $("#ajoutCom").fadeIn();
        }