CREATE VIEW [dbo].[FullInfo]
	AS 
	SELECT [p].[PersonId], [p].[FirstName], [p].[LastName], [i].[Email], [i].[NumerOfPets]
	FROM dbo.PersonalData p
	LEFT JOIN dbo.AdditionalInfo a ON p.PersonId = a.PersonId
	LEFT JOIN dbo.AdditionalInfo i on i.PersonId = p.PersonId;