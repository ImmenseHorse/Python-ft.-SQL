SELECT *,
       CASE
           WHEN GPA < 50
               THEN 'Failed'
           WHEN GPA = 50
               THEN 'Average'
           WHEN GPA BETWEEN 50
               AND 70
               THEN 'Good'
           ELSE 'Excellent'
           END AS Standing
FROM (SELECT `Name`,
             Class,
             `Subject`,
             AVG(Score) AS GPA
      FROM students
      GROUP BY `Name`
      ORDER BY GPA DESC) alias