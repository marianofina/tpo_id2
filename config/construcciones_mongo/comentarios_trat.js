db.createCollection(
    "comentarios_trat", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["id_trat", "id_medi", "fecha", "comentario"],
      properties: {
        _id: {
          bsonType: "objectId"
        },
        id_trat: {
          bsonType: "objectId",
          description: "Debe ser un objectId y es requerido"
        },
        id_medi: {
          bsonType: "string",
          description: "Debe ser un id sql (string) y es requerido"
        },
        comentario: {
            bsonType: "string",
            description: "Debe ser una cadena de texto y es requerido"
        },
        fecha: {
            bsonType: "string",
            description: "Debe ser una cadena de texto y es requerido"
        }
      }
    }
  }
})