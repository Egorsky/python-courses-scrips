CREATE PROCEDURE [dbo].[spPerson_FilterByFirstName]
	@FirstName nvarchar(50)

AS
BEGIN
	SELECT *
	FROM dbo.PersonalData
	WHERE FirstName = @FirstName
END