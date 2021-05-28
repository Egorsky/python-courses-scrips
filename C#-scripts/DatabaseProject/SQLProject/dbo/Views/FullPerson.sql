CREATE	 VIEW [dbo].[FullPerson]
	AS 
			SELECT  [p].[FirstName], [p].[LastName], 
			[a].[Id] AS AdressId, [a].[StreetAdress], 
			[a].[City], [a].[State], [a].[ZipCode]
			FROM dbo.PersonalData p
			LEFT JOIN dbo.Adress a on p.[PersonId] = a.PersonId
