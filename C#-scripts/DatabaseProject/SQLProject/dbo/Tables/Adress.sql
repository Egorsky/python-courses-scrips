CREATE TABLE [dbo].[Adress]
(
	[Id] INT NOT NULL PRIMARY KEY IDENTITY, 
    [PersonId] INT NOT NULL, 
    [StreetAdress] NVARCHAR(50) NULL, 
    [City] NVARCHAR(50) NULL, 
    [State] NVARCHAR(50) NULL, 
    [ZipCode] NVARCHAR(50) NULL, 
    CONSTRAINT [FK_Adress_Person] FOREIGN KEY ([PersonID]) REFERENCES [PersonalData]([PersonId])
)
