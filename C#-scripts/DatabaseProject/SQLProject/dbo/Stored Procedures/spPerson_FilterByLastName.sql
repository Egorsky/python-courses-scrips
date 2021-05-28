CREATE PROCEDURE [dbo].[spPerson_FilterByLastName]
	@LastName nvarchar(50)
AS
begin
	select [PersonId], [FirstName], [LastName]
	from dbo.PersonalData
	where LastName = @LastName
end