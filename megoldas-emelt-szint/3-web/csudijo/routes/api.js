var express = require('express')
var router = express.Router()
var mysql = require('mysql')
var sqlTasks = require('../assets/sqlTasks.json')
var db = {
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'csudijo'
}
const getSqlTasks = require('../assets/sqlTasks')

const databaseQuery = sqlQuery => {
    return new Promise((resolve, reject) => {
        const connection = mysql.createConnection(db)
        connection.connect()
        console.log('sqlQuery', sqlQuery)
        connection.query(sqlQuery, (error, lines, fields) => {
            if (error) reject(error)
            resolve(lines)
        })
    })
}

/* fech data from database */
router.get('/lekerdezes/:id', function(req, res, next) {
    getSqlTasks().then(result => {
        const sqlTasks = result
        console.log('sqlTasks', sqlTasks)
        const sqlTaskById = sqlTasks.filter(task => task.id == req.params.id)

        if (sqlTaskById) {
            sqlTask = sqlTaskById[0]
            if (sqlTask.sql) {
                databaseQuery(sqlTask.sql)
                    .then(result => {
                        res.send(JSON.stringify(result))
                    })
                    .catch(error => {
                        res.status(error.status || 500)
                        if (error.sqlMessage) {
                            console.log(error.sqlMessage)
                            res.send(JSON.stringify({ error: error.sqlMessage }))
                        } else {
                            console.log(JSON.stringify(error))
                            res.send(JSON.stringify({ error: 'Ismeretlen eredetű error' }))
                        }
                    })
            }
        }
    })
})

/* GET legnepszerubb. */
router.get('/legnepszerubb', function(req, res, next) {
    res.send(JSON.stringify({ etelNev: 'LECSÓ KOLBÁSZCSIPSSZEL' }))
})

/* GET sqlTasks */
router.get('/sqltasks', function(req, res, next) {
    res.send(JSON.stringify(sqlTasks))
})

/* POST vendegkonyv */
router.post('/vendegkonyv', function(req, res, next) {

    console.log(req.body)
    if (req.body.bejegyzes) {
        let sql = ''
        sql += 'CREATE TABLE IF NOT EXISTS vendegkonyv  '
        sql += '(bejegyzes longtext COLLATE utf8_hungarian_ci NOT NULL, '
        sql += 'createdAt timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP) '
        sql += 'ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;'
        databaseQuery(sql)
            .then(result => {
                console.log('result', result)
                sql = `INSERT INTO vendegkonyv (bejegyzes) VALUES ("${req.body.bejegyzes}");`
                databaseQuery(sql)
                    .then(result => {
                        console.log('result2', result)
                        res.send(JSON.stringify(req.body))
                    })
                    .catch(error => {
                        console.log('result2', error)
                        res.send(JSON.stringify(error))
                    })
            })
            .catch(error => {
                console.log('result', error)
                res.send(JSON.stringify(error))
            })
    }
})

module.exports = router