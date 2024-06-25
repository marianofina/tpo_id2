db.createCollection(
    "hospitalizaciones", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["id_paci", "id_medi", "fecha_ingreso", "tratamientos"],
      properties: {
        _id: {
          bsonType: "objectId"
        },
        paci_id: {
          bsonType: "string",
          description: "Debe ser un id sql (string) y es requerido"
        },
        id_medi: {
          bsonType: "string",
          description: "Debe ser un id sql (string) y es requerido"
        },
        fecha_ingreso: {
          bsonType: "string",
          description: "Debe ser una cadena de texto y es requerido"
        },
        fecha_alta: {
          bsonType: "string",
          description: "Debe ser una cadena de texto y es requerido"
        },
        tratamientos: {
          bsonType: "array",
          description: "Debe ser un array y es requerido",
          items: {
            bsonType: "objectId",
            description: "Debe ser un _id de mongoDB y es requerido"
          }
        }
      }
    }
  }
})