db.createCollection("tratamientos_medicos", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["paci_id", "id_medi", "diagnostico", "plan", "fecha_inicio", "fecha_fin", "status"],
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
        diagnostico: {
          bsonType: "string",
          description: "Debe ser una cadena de texto y es requerido"
        },
        plan: {
          bsonType: "array",
          description: "Debe ser un array y es requerido",
          items: {
            bsonType: "object",
            required: ["type", "details"],
            properties: {
              type: {
                bsonType: "string",
                description: "Tipo de plan, puede ser 'medicamento', 'terapia', 'cambio de estilo de vida', etc."
              },
              details: {
                bsonType: "string",
                description: "Detalles específicos del plan"
              }
            }
          }
        },
        fecha_inicio: {
          bsonType: "string",
          description: "Debe ser una string y es requerido"
        },
        fecha_fin: {
          bsonType: "string",
          description: "Debe ser una string y es requerido"
        },
        status: {
          bsonType: "string",
          description: "Estado del tratamiento, debe ser una cadena de texto y es requerido"
        }
      }
    }
  }
})